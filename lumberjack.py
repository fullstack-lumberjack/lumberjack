#!/usr/bin/env python3

import sys
# import logic
# import apache
# import ufw
import network

# if sys.argv[2] == '-t':
#     print(logic.type_of_log())

def main():
    switcher = {
        # "-a": apache.common()
        # ,
        # "-u": ufw(),
        "-n": network.main()
    }
    print(switcher.get(sys.argv[2], "invalid log"))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")
    else: main()