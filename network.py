import sys
import re

def main():
    result = ""
    for option in sys.argv[3:]:
        # if option == '-t':
        #     print(type_of_log())
        if option == '-num':
            result += num_unique_ips()
        if option == '-m':
            result += most_common_ips()
        if option == '-l':
            result += least_common_ips()
    return result.strip()

def num_unique_ips():
    ips = set()
    lines = open(sys.argv[1]).readlines()
    for l in lines:
        items = l.split(' ')
        if len(items) > 13:
            src = items[11] 
            src = src.split('=')[1]
            dst = items[12]
            dst = dst.split('=')[1]
            ips.add(src)
            ips.add(dst)
        else:
            pass
    return str(len(ips)) + '\n'

def most_common_ips():
    f = open(sys.argv[1], 'r').read()
    
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", f)

    ip_dict = {}

    for ip in all_ips_li: 
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)
    result=""
    for ip in sorted_dict[:5]:
        # print(ip, ip_dict[ip])
        result+= str(ip) + " " + str(ip_dict[ip]) + "\n"
    return result
    

def least_common_ips():
    f = open(sys.argv[1], 'r').read()
    
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", f)

    ip_dict = {}

    for ip in all_ips_li: 
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)
    result = ""
    for ip in sorted_dict[-5:]:
        result+= str(ip) + " " + str(ip_dict[ip]) + "\n"
    return result

