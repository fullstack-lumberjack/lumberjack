#!/usr/bin/env python3

import sys
import logic
import apache
import ufw
import network

# if sys.argv[2] == '-t':
#     print(logic.type_of_log())

def main():
    # if sys.argv[2] == 
    
    switcher = {
        "web server log": apache.common(),
        # "linux firewall log": ufw(),
        "network log": network.main()
    }
    print(switcher.get(logic.type_of_log().strip(), "invalid log"))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")
    else: main()