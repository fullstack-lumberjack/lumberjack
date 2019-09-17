import sys

def main():
    for option in sys.argv[2:]:
        if option == '-t':
            print(type_of_log())
        if option == '-n':
            print(num_unique_ips())
    # if sys.argv[3] == "":
    #print(unique_ips())

def num_unique_ips():
    ips = set()
    f = open(sys.argv[1])
    lines = f.readlines()
    if type_of_log() == "network server log":
        for l in lines:
            items = l.split(' ')
            if len(items) > 13:
                src = items[11] 
                src = src.split('=')[1]
                dst = items[12]
                dst = dst.split('=')[1]
                ips.add(src)
                ips.add(dst)
            else:
                pass
        return len(ips)
    if type_of_log() == "web server log":
        for l in lines:
            items = l.split(' ')
            ips.add(items[0])
        return len(ips)
    if type_of_log() == "firewall log":
        for l in lines:
            items = l.split(' ')
            src = items[9].split('=')[1]
            dst = items[10].split('=')[1]
            ips.add(src)
            ips.add(dst)
        return len(ips)

def type_of_log():
    f = open(sys.argv[1])
    lines = f.readlines()
    log = ""
    for l in lines:
        if "BLOCK" in l: 
            log = "firewall log"
        if ("GET" or "HEAD") in l:
            log = "web server log"
        if ("INBOUND" or "OUTBOUND") in l:
            log = "network server log"
    return log
    # ufw === BLOCK
    # web === GET or HEAD
    # network === INBOUND OR OUTBOUND