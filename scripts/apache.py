import sys
import re
import colorama

colorama.init()

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
RESET = '\033[0m'
YELLOW = '\033[33m'

def apache_status_code():
    content = open(sys.argv[1], 'r').read()
    apache_list = re.findall(r'(?<=\"\ )[0-9]{3}(?=\ )', content)
    
    apache_set = set()
    for code in apache_list:
        apache_set.add(code)
    if len(apache_set) == 0:
        print(f'There were no status codes found.')
    if len(apache_set) == 1:
        print(YELLOW+f'This status code was found: '+RESET+f'{apache_set}')
    if len(apache_set) > 1:
        print(YELLOW+f'These status codes were found: '+RESET+f'{apache_set}')
    return "END OF OUTPUT"

def apache_request_code():
    content = open(sys.argv[1], 'r').read()
    apache_request_list = re.findall(r'(?<=]\ \")[A-Za-z]{3,4}(?=\ )', content)
    apache_request_dict = {}
    for request in apache_request_list:
        if request not in apache_request_dict:
            apache_request_dict[request] = 1
        elif request in apache_request_dict:
            apache_request_dict[request] += 1
    print(YELLOW+f'This is a count of the request codes: '+RESET+f'{apache_request_dict}')
    return "END OF OUTPUT"

def apache_ip_and_code():
    content = open(sys.argv[1], 'r').readlines()
    ip_and_code_dict = {}
    error_list = []
    for line in content:
        new_content = re.findall(r'([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)(?: [^\"]*\"[^\"]*\" )([4][0-9]{2})', line)
        #print(len(new_content))
        if len(new_content) > 0:
            #print(new_content[0][0])
            if new_content[0][1] in ip_and_code_dict:
                ip_and_code_dict[new_content[0][1]].append(new_content[0][0])
            else:
                ip_and_code_dict[new_content[0][1]] = [(new_content[0][0])]
    #print(ip_and_code_dict)

    for code, ips in ip_and_code_dict.items():
        if code == '400':
            #print(ips)
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 400 error code: '+RESET+f'{error_list}')
        if code == '401':
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 401 error code: '+RESET+f'{error_list}')
        if code == '403':
            #print(ips)
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 403 error code: '+RESET+f'{error_list}')
        if code == '404':
            #print(ips)
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 404 error code: '+RESET+f'{error_list}')
        if code == '405':
            #print(ips)
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 405 error code: '+RESET+f'{error_list}')
        if code == '406':
            #print(ips)
            error_list = list(set(ips))
            print(YELLOW+f'These ip addresses got a 406 error code: '+RESET+f'{error_list}')
    return 'Exit'
    # ip_and_code_dict = {}
    # for c in content:
    #     lines = c.split(' ')
    #     status_code = ''
    #     ip = lines[0]
    #     if lines[6] == 'HTTP/0.99"':
    #         status_code = lines[7]
    #     else: 
    #         status_code = lines[8]
        
    #     if int(status_code) >= 400 and int(status_code) <= 406:
    #         if status_code in ip_and_code_dict: ip_and_code_dict[status_code].add(ip)
    #         else: 
    #             ip_and_code_dict[status_code] = set()
    #             ip_and_code_dict[status_code].add(ip)
    # for status in ip_and_code_dict:
    #     if status == '403':
    #         print(YELLOW+f'These ips are attempting to access forbidden pages: '+RESET+f'{ip_and_code_dict[status]}')
    #     if status == '404':
    #         print(YELLOW+f'These ips are attempting to access pages that aren\'t found '+RESET+f'{ip_and_code_dict[status]}')
    #     return 'END OF OUTPUT'
