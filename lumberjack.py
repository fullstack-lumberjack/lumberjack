#!/usr/bin/env python3

import sys
# import interactive
from scripts import interactive

def main():
    interactive.interactive()

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("How to use: lumberjack <log> <option> Ex: $ lumberjack log.txt <-a>")
    else: main()