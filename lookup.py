#!/usr/bin/env python
import os
import sys
import json
import ipaddress
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple, Dict
from datetime import datetime

def separate_ip_types(ip_list: List[str]) -> Tuple[List[str], List[str]]:
    ipv4_list, ipv6_list = [], []
    for ip in ip_list:
        (ipv4_list if isinstance(ipaddress.ip_network(ip, strict=False), ipaddress.IPv4Network) else ipv6_list).append(ip)
    return ipv4_list, ipv6_list

def classify_asn_neighbours(asn_neighbour_list: List[Dict[str, str]]) -> Tuple[List[str], List[str]]:
    upstream, downstream = [], []
    for neighbour in asn_neighbour_list:
        (upstream if neighbour.get('type') == 'left' else downstream).append(neighbour.get('asn'))
    return upstream, downstream

def fetch_url(url: str) -> Dict:
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode())

def fetch_asn_data(asn: str) -> List[Dict]:
    urls = [
        f'https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}',
        f'https://stat.ripe.net/data/as-overview/data.json?resource=as{asn}',
        f'https://stat.ripe.net/data/asn-neighbours/data.json?resource={asn}'
    ]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        responses = list(pool.map(fetch_url, urls))
    return responses

def update_not_announced_prefixes(asn_dict: Dict, ip_list: List[str], ip_version: str) -> None:
    for prefix in ip_list:
        subnet = ipaddress.ip_network(prefix)
        response = fetch_url(f'https://stat.ripe.net/data/network-info/data.json?resource={subnet[0]}')
        asn_list = response.get('data', {}).get('asns', [])

        if asn_list:
            asn = asn_list[0]
            if asn in asn_dict:
                asn_dict[asn]['not_announced_prefixes'][f'{ip_version}_prefixes'].append(prefix)

def process_asn(asn: str) -> Tuple[str, Dict, List[str], List[str]]:
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

    return asn, asn_data, ipv4_prefixes, ipv6_prefixes

def get_asn_dict(country_code: str) -> Dict:
    response = fetch_url(f'https://stat.ripe.net/data/country-resource-list/data.json?resource={country_code}')
    json_response = response
    asn_list = json_response.get('data', {}).get('resources', {}).get('asn', [])
    ipv4_list = json_response.get('data', {}).get('resources', {}).get('ipv4', [])
    ipv6_list = json_response.get('data', {}).get('resources', {}).get('ipv6', [])
    
    asn_dict = {}
    all_ipv4_prefixes = set(ipv4_list)
    all_ipv6_prefixes = set(ipv6_list)
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_asn = {executor.submit(process_asn, asn): asn for asn in asn_list}
        for future in as_completed(future_to_asn):
            asn, asn_data, ipv4_prefixes, ipv6_prefixes = future.result()
            asn_dict[asn] = asn_data
            all_ipv4_prefixes -= set(ipv4_prefixes)
            all_ipv6_prefixes -= set(ipv6_prefixes)
    
    update_not_announced_prefixes(asn_dict, list(all_ipv4_prefixes), 'ipv4')
    update_not_announced_prefixes(asn_dict, list(all_ipv6_prefixes), 'ipv6')
    
    return asn_dict

def write_to_file(content: Dict, filename: str, num_indent: int) -> None:
    with open(filename, 'w') as file:
        json.dump(content, file, indent=num_indent)

def main(country_code: str, num_indent: int) -> None:
    asn_dict = get_asn_dict(country_code)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{country_code}_asn_data_{timestamp}.json"
    
    write_to_file(asn_dict, filename, num_indent)
    print(f"ASN data written to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        script_name = os.path.basename(__file__)
        print(f'Usage:\t\tpython3 {script_name} [country_code] [num_indent]\n')
        print(f'Example:\tpython3 {script_name} fo')
        print(f'\t\tpython3 {script_name} fo 4')
    else:
        country_code = sys.argv[1]
        num_indent = int(sys.argv[2]) if len(sys.argv) > 2 else 4
        main(country_code, num_indent)
