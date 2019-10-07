import sys
import re
import colorama
from prettytable import PrettyTable

colorama.init()

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

print('''
  _                      _                    _            _    
 | |                    | |                  | |          | |   
 | |     _   _ _ __ ___ | |__   ___ _ __     | | __ _  ___| | __
 | |    | | | | '_ ` _ \| '_ \ / _ \ '__|_   | |/ _` |/ __| |/ /
 | |____| |_| | | | | | | |_) |  __/ |  | |__| | (_| | (__|   < 
 |______|\__,_|_| |_| |_|_.__/ \___|_|   \____/ \__,_|\___|_|\_\ 

''')

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

def create_table(dictionary, sorted_list, header1, header2, amount):
    t = PrettyTable([header1, header2])

    for i in range(0, amount):
        ip = sorted_list[i]
        t.add_row([ip, dictionary[ip]])
    
    return t

def unique_ips(ip_set):
    return f'There are {len(ip_set)} unique ips.'
    
def print_ip_table(ip_dictionary, direction=True):
    sorted_list = sorted(ip_dictionary,key=lambda ip: ip_dictionary[ip], reverse=direction)

    if direction == True:
        print(YELLOW+'These are the top 5 most occurring ips:'+RESET)
    else:
        print(YELLOW+'These are the top 5 least occurring ips:'+RESET)

    return create_table(ip_dictionary, sorted_list, 'IP ADDRESS', 'OCCURRENCE', 5)

def create_port_dictionaries():
    content = open(sys.argv[1], 'r').read()
    all_source_ports = re.findall(r"SPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", content)
    all_dest_ports = re.findall(r"DPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", content)
    
    port_dict = {}
    port_set = set()
    for port in all_source_ports: 
        if port in port_dict: port_dict[port] += 1
        else: port_dict[port] = 1
    for port in all_dest_ports: 
        if port in port_dict: port_dict[port] += 1
        else: port_dict[port] = 1
    return [port_dict, port_set]

def most_ports(port_dict):
    reverse_sorted = sorted(port_dict, key=lambda port: port_dict[port], reverse=True)
    print(YELLOW+'These are the top 5 most occurring ports:'+RESET)

    return create_table(port_dict, reverse_sorted, 'IP ADDRESS', 'OCCURRENCE', 5)
    
def type_of_log():
    f = open(sys.argv[1])
    lines = f.readlines()
    log = ""
    for l in lines:
        if "BLOCK" in l: 
            log = "linux firewall log"
        elif ("GET" or "HEAD") in l:
            log = "web server log"
        elif ("INBOUND" or "OUTBOUND") in l:
            log = "network log"
        else:
            log = "Daylight in the swamp!"
    return log