import sys
import re

def create_dictionaries():
    content = open(sys.argv[1], 'r').read()
    all_ips = re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', content)

    ip_dictionary = {}
    ip_set = set()

    for ip in all_ips:
        ip_set.add(ip)
        if ip in ip_dictionary: ip_dictionary[ip] += 1
        else: ip_dictionary[ip] = 1 
    
    return [ip_dictionary, ip_set]

big_dictionary = create_dictionaries()
ip_dictionary = big_dictionary[0]
ip_set = big_dictionary[1]

def unique_ips():
    print(f'There are {len(ip_set)} unique ips.')

def compare_value(ip):
    return ip_dictionary[ip]

def most_ips():
    reverse_sorted = sorted(ip_dictionary, key=compare_value, reverse=True)

    print('\nThese are the top 5 most occurring ips:')
    for ip in reverse_sorted[:5]:
        print(f'ip: {ip}, occurrence: {ip_dictionary[ip]}')
    
def least_ips():
    sorted_ip_list = sorted(ip_dictionary, key=compare_value, reverse=False)

    print('\nThese are the top 5 least occurring ips:')
    for ip in sorted_ip_list[:5]:
        print(f'ip: {ip}, occurrence: {ip_dictionary[ip]}')