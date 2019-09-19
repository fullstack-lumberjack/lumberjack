#!/usr/bin/env python3

import sys
from scripts import utility, options, ufw_status, apache
import interactive

def main():
    # log_type = utility.type_of_log()
    # print(f'\nYou are looking at a {log_type}.\n')

    # switcher = {
    # '--unique': utility.unique_ips,
    # '--most': utility.most_ips,
    # '--least': utility.least_ips,
    # '--astatus': apache.apache_status_code,
    # '--arequest': apache.apache_request_code,
    # '--aip': apache.apache_ip_and_code
    # }
    # print(switcher.get(sys.argv[2], options.print_option)())
    interactive.interactive()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack <log> <option> Ex: $ lumberjack log.txt <-a>")
    # elif len(sys.argv) == 2: utility.print_all_ips()
    else: main()