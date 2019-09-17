import sys
import logic
# import apache
# import ufw
# import network

# -h 
if len(sys.argv) <= 1 or sys.argv[1] == '-h':
    print("How to use: lumberjack.py <logfile> <logtype>. Ex: lumberjack.py log.txt -a")

# if sys.argv[2] == '-t':
#     print(logic.type_of_log())

# def main():
#     switcher = {
#         "-a": apache(),
#         "-u": ufw(),
#         "-n": network()
#     }
#     print(switcher.get(arg, "invalid log"))

# if __name__ == '__main__':
#     main()