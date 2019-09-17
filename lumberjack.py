import sys
import logic
# import apache
# import ufw
import network

# unique (num)
# top 5
# least 5

# -h 
# if len(sys.argv) <= 1 or sys.argv[1] == '-h':
#     print("Input like this: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")

if sys.argv[2] == '-t':
    print(logic.type_of_log())

def switch(arg):
    switcher = {
        # "-a": apache(),
        # "-u": ufw(),
        "-n": network.main("-t")
    }
    print(switcher.get(arg, "invalid log"))

switch(sys.argv[2])

def main():
    return

if __name__ == '__main__':
    main()