#!/usr/bin/env python3

import sys
from scripts import utility
from scripts import options

def main():
    log_type = utility.type_of_log()
    print(f'\nYou are looking at a {log_type}.\n')

    print(utility.unique_ips())
    print(utility.most_ips())
    print(utility.least_ips())

    if len(sys.argv) >= 3:
        options.print_option(sys, log_type)

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack <log> <option> Ex: lumberjack.py log.txt <-a>")
    else: main()