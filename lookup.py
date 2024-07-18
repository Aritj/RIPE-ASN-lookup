#!/usr/bin/env python
import os
import sys
import json
import ipaddress
from requests import get, Response
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple, Dict
from datetime import datetime

def separate_ip_types(ip_list: List[str]) -> Tuple[List[str], List[str]]:
    ipv4_list = [ip for ip in ip_list if isinstance(ipaddress.ip_network(ip, strict=False), ipaddress.IPv4Network)]
    ipv6_list = [ip for ip in ip_list if isinstance(ipaddress.ip_network(ip, strict=False), ipaddress.IPv6Network)]
    return ipv4_list, ipv6_list

def fetch_asn_data(asn: str) -> List[Dict]:
    urls = [
        f'https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}',
        f'https://stat.ripe.net/data/as-overview/data.json?resource=as{asn}'
    ]
    with ThreadPoolExecutor(max_workers=2) as pool:
        responses = list(pool.map(get, urls))
    return [response.json() for response in responses]

def update_not_announced_prefixes(asn_dict: Dict, ip_list: List[str], ip_version: str) -> None:
    for prefix in ip_list:
        subnet = ipaddress.ip_network(prefix)
        response = get(f'https://stat.ripe.net/data/network-info/data.json?resource={subnet[0]}')
        asn_list = response.json().get('data', {}).get('asns', [])

        if asn_list:
            asn = asn_list[0]
            if asn in asn_dict:
                asn_dict[asn]['not_announced'][f'{ip_version}_prefixes'].append(prefix)

def get_asn_dict(country_code: str) -> Dict:
    response = get(f'https://stat.ripe.net/data/country-resource-list/data.json?resource={country_code}')
    json_response = response.json()
    asn_list = json_response.get('data', {}).get('resources', {}).get('asn', [])
    ipv4_list = json_response.get('data', {}).get('resources', {}).get('ipv4', [])
    ipv6_list = json_response.get('data', {}).get('resources', {}).get('ipv6', [])
    
    asn_dict = {}
    
    for asn in asn_list:
        asn_prefix_json_response, asn_overview_json_response = fetch_asn_data(asn)
        
        prefix_entries = asn_prefix_json_response.get('data', {}).get('prefixes', [])
        prefixes = [entry.get('prefix') for entry in prefix_entries]
        as_name = asn_overview_json_response.get('data', {}).get('holder', "Unknown Holder")
        ipv4_prefixes, ipv6_prefixes = separate_ip_types(prefixes)

        ipv4_list = list(set(ipv4_list) - set(ipv4_prefixes))
        ipv6_list = list(set(ipv6_list) - set(ipv6_prefixes))

        asn_dict[asn] = {
            'name': as_name,
            'announced': {'ipv4_prefixes': ipv4_prefixes, 'ipv6_prefixes': ipv6_prefixes},
            'not_announced': {'ipv4_prefixes': [], 'ipv6_prefixes': []}
        }
    
    update_not_announced_prefixes(asn_dict, ipv4_list, 'ipv4')
    update_not_announced_prefixes(asn_dict, ipv6_list, 'ipv6')
    
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
        print(f'Example:\tpython3 {script_name} fo 4')
    else:
        country_code = sys.argv[1]
        num_indent = int(sys.argv[2]) if len(sys.argv) > 2 else None
        main(country_code, num_indent)
