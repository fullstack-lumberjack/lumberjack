import sys
import logic
# import apache
# import ufw
# import network

# -h 
# if len(sys.argv) <= 1 or sys.argv[1] == '-h':
#     print("Input like this: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")

if sys.argv[2] == '-t':
    print(logic.type_of_log())

def switch(arg):
    switcher = {
        "-a": apache(),
        "-u": ufw(),
        "-n": network()
    }
    print(switcher.get(arg, "invalid log"))


def main():
    return

if __name__ == '__main__':
    main()