import sys
import re

def main(opt):
    for option in sys.argv[3:]:
        # if option == '-t':
        #     print(type_of_log())
        if option == '-num':
            print(num_unique_ips())
        if option == '-m':
            print(most_common_ips())
        if option == '-l':
            print(least_common_ips())

def num_uniq_ips():
    ips = set()
    f = open(sys.argv[1])
    lines = f.readlines()
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
    return len(ips)

def most_common_ips():
    f = open(sys.argv[1])
    lines = f.readlines()
    
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", lines)

    ip_dict = {}

    for ip in all_ips_li: 
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)

    for ip in sorted_dict[:5]:
        print(ip, ip_dict[ip])

def least_common_ips():
    f = open(sys.argv[1])
    lines = f.readlines()
    
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", lines)

    ip_dict = {}

    for ip in all_ips_li: 
        if ip in ip_dict: ip_dict[ip] += 1
        else: ip_dict[ip] = 1

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)

    for ip in sorted_dict[-5:]:
        print(ip, ip_dict[ip])

