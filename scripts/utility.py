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

def unique_ips(ip_set):
    print(f'There are {len(ip_set)} unique ips.')
    return 'FINISHED\n'

def most_ips(ip_dictionary):
    reverse_sorted = sorted(ip_dictionary, key=lambda ip: ip_dictionary[ip], reverse=True)

    print(YELLOW+'These are the top 5 most occurring ips:'+RESET)

    t = PrettyTable(['IP ADDRESS', 'OCCURRENCE'])

    for ip in reverse_sorted[:5]:
        t.add_row([ip, ip_dictionary[ip]])
        # print(CYAN+'ip: ' + RESET+GREEN+f'{ip}' +RESET+CYAN+ ', occurrence: '+ RESET+GREEN+f'{ip_dictionary[ip]}'+RESET)
    print(t)
    return 
    
def least_ips(ip_dictionary):
    sorted_ip_list = sorted(ip_dictionary, key=lambda ip: ip_dictionary[ip], reverse=False)

    print(YELLOW+'These are the top 5 least occurring ips:'+RESET)

    t = PrettyTable(['IP ADDRESS', 'OCCURRENCE'])
    for ip in sorted_ip_list[:5]:
        t.add_row([ip, ip_dictionary[ip]])
        # print(CYAN+'ip: ' + RESET+GREEN+f'{ip}' +RESET+CYAN+ ', occurrence: '+ RESET+GREEN+f'{ip_dictionary[ip]}'+RESET)
    print(t)
    return

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
    
    t = PrettyTable(['PORT', 'OCCURRENCE'])
    
    for port in reverse_sorted[:5]:
        t.add_row([port, port_dict[port]])
        # print(f'port: {port}, occurrences: {port_dict[port]}')
    
    print(t)
    return

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

def print_all_ips(ip_dictionary, ip_set):
    print(unique_ips(ip_set))
    print(most_ips(ip_dictionary))
    print(least_ips(ip_dictionary))

def print_ips(argv):

    switcher = {
        '--unique': unique_ips,
        '--most': most_ips,
        '--least': least_ips,
    }
    print(switcher.get(argv[2], )())

# big_dictionary = []
# ip_dictionary = {}
# ip_set = {}

# big_port_dictionary = {}
# port_dict = []
# port_set = {}

# if len(sys.argv) >= 2:
#     big_dictionary = create_dictionaries()
#     ip_dictionary = big_dictionary[0]
#     ip_set = big_dictionary[1]

#     big_port_dictionary = create_port_dictionaries()
#     port_dict = big_port_dictionary[0]
#     port_set = big_port_dictionary[1]