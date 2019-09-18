from scripts import ufw_status
from scripts import utility

def print_option(sys, log_type):
    if log_type == 'linux firewall log':
        if sys.argv.index('-sc'):
            print(ufw_status.ufw_status_code())

        if sys.argv.index('-p'):
            print(ufw_status.ufw_protocol())
    
    if log_type == 'network log':
        if sys.argv.index('-pm'):
            utility.most_ports()
    