import sys
import re
import logic

def main():
    result = ""
    for option in sys.argv[2:]:
        if option == '-u' or option == '-su' or option == '-du':
            result += num_unique_ips()
        if option == '-m' or option == '-l' or option == '-sim' or option == '-dim':
            result += most_common_ips()
        if option == '-t':
            result += logic.type_of_log()
        if option == '-pm' or option == '-spm' or option == '-dpm':
            result += ports()

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
            for option in sys.argv[2:]:
                if option == '-su':
                    ips.add(src)
                elif option == '-du':
                    ips.add(dst)
                else:
                    ips.add(src)
                    ips.add(dst)
        else:
            pass
    return str(len(ips)) + '\n'

def most_common_ips():
    f = open(sys.argv[1], 'r').read()
    
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", f)
    src_ips_li = re.findall(r"SRC=[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", f)
    dst_ips_li = re.findall(r"DST=[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", f)
    
    ip_dict = {}
    
    for option in sys.argv[2:]:
        if option == '-sim':
            for ip in src_ips_li: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
        if option == '-dim':
            for ip in dst_ips_li: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
        if option == '-m' or option == '-l':
            for ip in all_ips_li: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
                

    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)
    result=""
    for option in sys.argv[2:]:
        if option == "-l":
            for ip in sorted_dict[-5:]:
                result += str(ip) + " " + str(ip_dict[ip]) + "\n"
        else:
            for ip in sorted_dict[:5]:
                if option == '-m':
                    result += str(ip) + " " + str(ip_dict[ip]) + "\n"
                else: result += str(ip)[4:] + " " + str(ip_dict[ip]) + "\n"
    return result


def ports():
    f = open(sys.argv[1], 'r').read()
    s_ports = re.findall(r"SPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", f)
    d_ports = re.findall(r"DPT=([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])", f)
    ip_dict = {}
    for option in sys.argv[2:]:
        if option == '-spm':
            for ip in s_ports: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
        if option == '-dpm':
            for ip in d_ports: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
        if option == '-pm':
            for ip in s_ports: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1
            for ip in d_ports: 
                if ip in ip_dict: ip_dict[ip] += 1
                else: ip_dict[ip] = 1 
    def compare_count(ip):
        return ip_dict[ip]

    sorted_dict = sorted(ip_dict, key=compare_count, reverse=True)
    result = ""
    for ip in sorted_dict[:5]:
        result+= str(ip) + " " + str(ip_dict[ip]) + "\n"
    return result