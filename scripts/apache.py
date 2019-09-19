import sys
import re

def apache_status_code():
    content = open(sys.argv[1], 'r').read()
    apache_list = re.findall(r'(?<=\"\ )[0-9]{3}(?=\ )', content)
    
    apache_set = set()
    for code in apache_list:
        apache_set.add(code)
    if len(apache_set) == 0:
        return f'There were no status codes found.'
    if len(apache_set) == 1:
        return f'This status code was found: {apache_set}'
    if len(apache_set) > 1:
        return f'These status codes were found: {apache_set}'

def apache_request_code():
    content = open(sys.argv[1], 'r').read()
    apache_request_list = re.findall(r'(?<=]\ \")[A-Za-z]{3,4}(?=\ )', content)
    apache_request_dict = {}
    for request in apache_request_list:
        if request not in apache_request_dict:
            apache_request_dict[request] = 1
        elif request in apache_request_dict:
            apache_request_dict[request] += 1
    return f'This is a count of the request codes: {apache_request_dict}'


def apache_ip_and_code():
    content = open(sys.argv[1], 'r').readlines()
    
    ip_and_code_dict = {}

    for c in content:
        lines = c.split(' ')
        status_code = ''
        ip = lines[0]
        if lines[6] == 'HTTP/0.99"':
            status_code = lines[7]
        else: 
            status_code = lines[8]
        
        if int(status_code) >= 400 and int(status_code) <= 406:
            if status_code in ip_and_code_dict: ip_and_code_dict[status_code].add(ip)
            else: 
                ip_and_code_dict[status_code] = set()
                ip_and_code_dict[status_code].add(ip)
    for status in ip_and_code_dict:
        if status == '403':
            return f'These ips are attempting to access forbidden pages {ip_and_code_dict[status]}'
        if status == '404':
            return f'These ips are attempting to access pages that aren\'t found {ip_and_code_dict[status]}'


    # lst = []
    # dict = {}

    # for line in content:
    #     apache_code = re.match(r'(?<=\"\ )[0-9]{3}(?=\ )', line)   
    #     if apache_code == True:
    #         lst.append(line)
    #     print(lst)
    # for line in lst:
    #     ip = re.match(r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', lst)
    #     new_lst = lst.split(' ')

    #     for l in new_lst:
    #         if l not in dict:
    #             dict[l] = set()
    #             dict[l].add(ip)
    #         else:
    #             dict[l].add(ip)
