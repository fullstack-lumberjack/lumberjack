import sys
import logic
import re

def main():
    for option in sys.argv[3:]:
        if option == '-n':
            print(num_of_unique_ips())
         
def num_of_unique_ips():
    f = open(sys.argv[1])
    all_ips_li = f.readlines()
    all_ips_li = re.findall(r"[0-9]+\.[0-9]+\.[0-9]+.[0-9]+", content)
    print(all_ips_li)
    ip_dict = {}
    for ip in all_ips_li: 
        if ip in ip_dict: 
            ip_dict[ip] += 1
        else: 
            ip_dict[ip] = 1
    #print(ip_dict)

if __name__ == '__main__':
    main()
