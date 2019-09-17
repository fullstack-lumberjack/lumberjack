#!/usr/bin/env python3

import sys
import utility

def main():
    print(utility.common())

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")
    else: main()