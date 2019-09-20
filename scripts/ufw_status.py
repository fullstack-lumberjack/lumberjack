#!/usr/bin/env python3
import sys
import re
import colorama

colorama.init()

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

def ufw_status_code():
    content = open(sys.argv[1], 'r').read()
    
    block_list = re.findall(r'(?<=BLOCK]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    block_set = set()
    for ip in block_list:
        block_set.add(ip)
    print(f'These are the blocked ips: '+YELLOW+f'{block_set}' +RESET+'\n')
 
    allow_list = re.findall(r'(?<=ALLOW]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    allow_set = set()
    for ip in allow_list:
        allow_set.add(ip)
    print(f'These are the allowed ips: '+YELLOW+f'{allow_set}' +RESET+'\n')

    audit_list = re.findall(r'(?<=AUDIT]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    audit_set = set()
    for ip in audit_list:
        audit_set.add(ip)
    print(f'These are the audited ips:' +YELLOW+ f'{audit_set}'+RESET)
    return 'FINISHED'
    
def ufw_protocol():
    content = open(sys.argv[1], 'r').read()
    
    protocol_list = re.findall(r'(?<=PROTO=).+(?=\ SPT)', content)
    protocol_set = set()
    for p in protocol_list:
        protocol_set.add(p)
    return f'These are the protocols used: {protocol_set}'
    
if __name__ == '__main__':
    main()