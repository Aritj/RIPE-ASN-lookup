#!/usr/bin/env python
import json
import argparse
import ipaddress
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict, Union
from datetime import datetime

def separate_ip_types(ip_list: List[str]) -> Tuple[List[str], List[str]]:
    """
    Separates a list of IP addresses into IPv4 and IPv6 addresses.

    Args:
        ip_list (List[str]): List of IP addresses.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists - IPv4 addresses and IPv6 addresses.
    """
    ipv4_list, ipv6_list = [], []

    for ip in ip_list:
        (ipv4_list if isinstance(ipaddress.ip_network(ip, strict=False), ipaddress.IPv4Network) else ipv6_list).append(ip)

    return ipv4_list, ipv6_list

def classify_asn_neighbours(asn_neighbour_list: List[Dict]) -> Tuple[List[str], List[str]]:
    """
    Classifies ASNs into upstream and downstream based on their type.

    Args:
        asn_neighbour_list (List[Dict]): List of ASN neighbours with their types.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists - upstream ASNs and downstream ASNs.
    """
    upstream, downstream = [], []

    for neighbour in asn_neighbour_list:
        (upstream if neighbour.get('type') == 'left' else downstream).append(neighbour.get('asn'))

    return upstream, downstream

def fetch_url(url: str) -> Dict:
    """
    Fetches data from a given URL and returns it as a dictionary.

    Args:
        url (str): The URL to fetch data from.

    Returns:
        Dict: The fetched data as a dictionary.
    """
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

def fetch_asn_data(asn: str) -> List[Dict]:
    """
    Fetches ASN data from multiple URLs concurrently.

    Args:
        asn (str): The ASN to fetch data for.

    Returns:
        List[Dict]: A list of dictionaries containing the fetched data.
    """
    urls = [
        f'https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}',
        f'https://stat.ripe.net/data/as-overview/data.json?resource=as{asn}',
        f'https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn}'
    ]

    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        return list(pool.map(fetch_url, urls))

def ip_range_to_cidr(start_ip: str, end_ip: str) -> List[ipaddress.IPv4Network]:
    """
    Converts an IP range to a list of CIDR blocks.

    Args:
        start_ip (str): The start IP of the range.
        end_ip (str): The end IP of the range.

    Returns:
        List[ipaddress.IPv4Network]: List of IPv4 CIDR blocks.
    """
    start = ipaddress.ip_address(start_ip)
    end = ipaddress.ip_address(end_ip)
    min_netmask_size = 0x100 # /24
    cidr_blocks = []

    while int(start) < int(end):
        count_24_netmasks = int((int(end) - int(start) + 1) / min_netmask_size)
        n = 1
        current_mask = 24

        while n << 1 <= count_24_netmasks:
            n <<= 1
            current_mask -= 1

        while True: # TODO: Should ideally be cleaned up
            try:
                cidr_blocks.append(ipaddress.ip_network(f'{start}/{current_mask}', strict=False))
                break
            except:
                n >>= 1
                current_mask += 1

        start = ipaddress.ip_address(int(start) + n*min_netmask_size)

    return cidr_blocks

def parse_ip(ip_str: str) -> List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]:
    """
    Parses an IP string that could be in CIDR or range format.

    Args:
        ip_str (str): The IP string to parse.

    Returns:
        List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]: List of CIDR blocks.
    """
    separator = '-'

    if separator not in ip_str:
        return [ipaddress.ip_network(ip_str, strict=False)]

    start_ip, end_ip = ip_str.split(separator)

    return ip_range_to_cidr(start_ip, end_ip)

def subtract_prefixes(large_prefix: Union[ipaddress.IPv4Network, ipaddress.IPv6Network], smaller_prefixes: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]) -> List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]:
    """
    Subtracts smaller prefixes from a larger prefix and returns the non-overlapping parts.

    Args:
        large_prefix (ipaddress.IPv4Network | ipaddress.IPv6Network): The larger prefix to subtract from.
        smaller_prefixes (List[ipaddress.IPv4Network] | List[ipaddress.IPv6Network]): The smaller prefixes to subtract.

    Returns:
        List[ipaddress.IPv4Network] | List[ipaddress.IPv6Network]: List of non-overlapping subnets.
    """
    remaining_prefixes = [large_prefix]

    for smaller in smaller_prefixes:
        temp = []

        for prefix in remaining_prefixes:

            if smaller.subnet_of(prefix):
                temp.extend(prefix.address_exclude(smaller))
            else:
                temp.append(prefix)

        remaining_prefixes = temp

    return remaining_prefixes

def process_prefix(prefix: str, asn_dict: Dict, ip_version: str) -> None:
    """
    Processes a single IP prefix to update the ASN dictionary with not announced prefixes.

    Args:
        prefix (str): The IP prefix to process.
        asn_dict (Dict): The ASN dictionary to update.
        ip_version (str): The IP version ('ipv4' or 'ipv6').
    """
    subnets = parse_ip(prefix)

    for subnet in subnets:
        response = fetch_url(f'https://stat.ripe.net/data/network-info/data.json?resource={subnet.network_address}')
        asn_list = response.get('data', {}).get('asns', [])

        if asn_list:
            asn = asn_list[0]
            if asn in asn_dict:
                announced_prefixes = [ipaddress.ip_network(ap) for ap in asn_dict[asn]['announced_prefixes'][f'{ip_version}_prefixes']]
                non_overlapping_subnets = subtract_prefixes(subnet, announced_prefixes)
                asn_dict[asn]['not_announced_prefixes'][f'{ip_version}_prefixes'].extend([str(p) for p in non_overlapping_subnets])

def update_not_announced_prefixes(asn_dict: Dict, ip_set: set, ip_version: str, thread_count: int) -> None:
    """
    Updates the ASN dictionary with not announced prefixes using multi-threading.

    Args:
        asn_dict (Dict): The ASN dictionary to update.
        ip_set (set): Set of IP prefixes.
        ip_version (str): The IP version ('ipv4' or 'ipv6').
        thread_count (int): The number of threads to use for concurrent processing.
    """
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        futures = [executor.submit(process_prefix, prefix, asn_dict, ip_version) for prefix in ip_set]
        for future in as_completed(futures):
            future.result()

def process_asn(asn: str) -> Tuple[str, Dict, set, set]:
    """
    Processes an ASN and returns its data along with announced prefixes.

    Args:
        asn (str): The ASN to process.

    Returns:
        Tuple[str, Dict, set, set]: A tuple containing the ASN, its data, announced IPv4 prefixes, and announced IPv6 prefixes.
    """
    announced_prefix, asn_overview, asn_neighbour = fetch_asn_data(asn)

    as_name = asn_overview.get('data', {}).get('holder', "Unknown Holder")
    announced_prefixes = announced_prefix.get('data', {}).get('prefixes', [])
    announced_prefixes = [entry.get('prefix') for entry in announced_prefixes]
    ipv4_prefixes, ipv6_prefixes = separate_ip_types(announced_prefixes)
    asn_neighbour_list = asn_neighbour.get('data', {}).get('neighbours', [])
    upstream, downstream = classify_asn_neighbours(asn_neighbour_list)

    asn_data = {
        'name': as_name,
        'upstream_bgp_asn': upstream,
        'downstream_bgp_asn': downstream,
        'announced_prefixes': {'ipv4_prefixes': ipv4_prefixes, 'ipv6_prefixes': ipv6_prefixes},
        'not_announced_prefixes': {'ipv4_prefixes': [], 'ipv6_prefixes': []}
    }

    return asn, asn_data, set(ipv4_prefixes), set(ipv6_prefixes)

def update_announced_prefixes(asn_dict: Dict, asn_list: List, ipv4_set: set, ipv6_set: set, thread_count: int):
    """
    Updates the ASN dictionary with announced prefixes using multi-threading.

    Args:
        asn_dict (Dict): The ASN dictionary to update.
        asn_list (List): List of ASNs to process.
        ipv4_set (set): Set of IPv4 prefixes.
        ipv6_set (set): Set of IPv6 prefixes.
        thread_count (int): The number of threads to use for concurrent processing.
    """
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        future_to_asn = {executor.submit(process_asn, asn): asn for asn in asn_list}
        for future in as_completed(future_to_asn):
            asn, asn_data, ipv4_prefixes, ipv6_prefixes = future.result()
            asn_dict[asn] = asn_data
            ipv4_set -= ipv4_prefixes
            ipv6_set -= ipv6_prefixes

def get_asn_dict(country_code: str, thread_count: int) -> Dict:
    """
    Retrieves the ASN dictionary for a given country code.

    Args:
        country_code (str): The country code to retrieve ASNs for.
        thread_count (int): The number of threads to use for concurrent processing.

    Returns:
        Dict: The ASN dictionary for the given country code.
    """
    country_resources = fetch_url(f'https://stat.ripe.net/data/country-resource-list/data.json?resource={country_code}')
    asn_list = country_resources.get('data', {}).get('resources', {}).get('asn', [])
    ipv4_list = country_resources.get('data', {}).get('resources', {}).get('ipv4', [])
    ipv6_list = country_resources.get('data', {}).get('resources', {}).get('ipv6', [])

    asn_dict = {}
    all_ipv4_prefixes = set(ipv4_list)
    all_ipv6_prefixes = set(ipv6_list)

    # Update ASN dictionary with announced
    update_announced_prefixes(asn_dict, asn_list, all_ipv4_prefixes, all_ipv6_prefixes, thread_count)

    # Update ASN dictionary with not announced prefixes
    update_not_announced_prefixes(asn_dict, all_ipv4_prefixes, 'ipv4', thread_count)
    update_not_announced_prefixes(asn_dict, all_ipv6_prefixes, 'ipv6', thread_count)

    return asn_dict

def write_to_file(content: Dict, filename: str, num_indent: int) -> None:
    """
    Writes the given content to a file in JSON format.

    Args:
        content (Dict): The content to write to the file.
        filename (str): The name of the file.
        num_indent (int): The number of spaces to use for indentation in the JSON file.
    """
    with open(filename, 'w') as file:
        json.dump(content, file, indent=num_indent)

def main(country_code: str, num_indent: Union[int, None], thread_count: int) -> None:
    """
    Main function to retrieve ASN data and write it to a file.

    Args:
        country_code (str): The country code to retrieve ASNs for.
        num_indent (Union[int, None]): The number of spaces to use for indentation in the JSON file.
        thread_count (int): The number of threads to use for concurrent processing.
    """
    asn_dict = get_asn_dict(country_code, thread_count)
    timestamp = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    filename = f"{country_code}_asn_data_{timestamp}.json"

    write_to_file(asn_dict, filename, num_indent)
    print(f"ASN data written to {filename}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ASN Data Lookup")
    parser.add_argument("country_code", help="The country code to retrieve ASNs for")
    parser.add_argument("-i", "--indent", type=int, default=None, help="The number of spaces to use for JSON output indentation")
    parser.add_argument("-t", "--threads", type=int, default=1, help="The number of threads to use for concurrent processing")
    args = parser.parse_args()

    main(args.country_code, args.indent, args.threads)
