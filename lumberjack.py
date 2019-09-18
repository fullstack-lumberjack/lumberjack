#!/usr/bin/env python3

import sys
from scripts import utility

def main():
    log_type = utility.type_of_log()
    print(f'You are looking at a {log_type}')

    if len(sys.argv) == 2: 
        print(utility.unique_ips())
        print(utility.most_ips())
        print(utility.least_ips())

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt <-a>")
    else: main()