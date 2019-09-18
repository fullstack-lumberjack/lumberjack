import sys
import re

def main():
    for option in sys.argv[2:]:
        if option == '-sc':
            print(ufw_status_code())
        if option == '-p':
            print(ufw_protocol())

def ufw_status_code():
    content = open(sys.argv[1], 'r').read()
    
    block_list = re.findall(r'(?<=BLOCK]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    block_set = set()
    for ip in block_list:
        block_set.add(ip)
    print(f'These are the blocked ips: {block_set} \n')
 
    allow_list = re.findall(r'(?<=ALLOW]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    allow_set = set()
    for ip in allow_list:
        allow_set.add(ip)
    print(f'These are the allowed ips: {allow_set} \n')

    audit_list = re.findall(r'(?<=AUDIT]\ IN=\ OUT=eth0\ SRC=)[0-9]+\.[0-9]+\.[0-9]+.[0-9]+(?=\ DST)', content)
    audit_set = set()
    for ip in audit_list:
        audit_set.add(ip)
    print(f'These are the audited ips: {audit_set}')
    return ' '
def ufw_protocol():
    content = open(sys.argv[1], 'r').read()
    
    protocol_list = re.findall(r'(?<=PROTO=).+(?=\ SPT)', content)
    protocol_set = set()
    for p in protocol_list:
        protocol_set.add(p)
    print(f'These are the protocols used: {protocol_set}')
    return ' '
if __name__ == '__main__':
    main()