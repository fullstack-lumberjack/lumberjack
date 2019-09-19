import sys
from scripts import ufw_status, utility, apache

def print_option():
    log_type = utility.type_of_log()

    if log_type == 'linux firewall log':
        switcher = {
            '--status': ufw_status.ufw_status_code,
            '--proto': ufw_status.ufw_protocol,
            '--astatus': apache.apache_status_code()
        }
        print(switcher.get(sys.argv[2], lambda: 'Option not found')())
    
    if log_type == 'network log':
        switcher = {
            '--ports': utility.most_ports
        }
        print(switcher.get(sys.argv[2], lambda: 'Option not found')())
    
    return 'END'
    