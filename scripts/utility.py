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

def make_dictionaries(list_of_elements):
    dictionary = {}
    unique = set()
    for item in list_of_elements:
        unique.add(item)
        if item in dictionary: 
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return [dictionary, unique]

def create_ip_dictionary():
    content = open(sys.argv[1], 'r').read()
    all_ips = re.findall(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', content)
    return make_dictionaries(all_ips)

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

def create_port_dictionary():
    content = open(sys.argv[1], 'r').read()
    all_source_ports = re.findall(r"SPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", content)
    all_dest_ports = re.findall(r"DPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", content)

    src_ports = make_dictionaries(all_source_ports)
    dst_ports = make_dictionaries(all_dest_ports)

    return {**src_ports[0], **dst_ports[0]}
    
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