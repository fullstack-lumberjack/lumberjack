from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import style_from_dict, Token, prompt, Separator
from examples import custom_style_2
from scripts import utility, apache, ufw_status

ip_dictionary, ip_set = utility.create_dictionaries()
port_dict, port_set = utility.create_port_dictionaries()

def interactive():

    firewall = [
        {
            'type': 'checkbox',
            'message': 'Select your options Press Ctrl+C to Exit',
            'name': 'Options',
            'choices': [ 
                Separator('= Type of log ='),
                {
                    'name': 'Type of log'
                },
                Separator('= Exit ='),
                {
                    'name': 'Exit'
                },
                Separator('= Status Codes (Firewall logs) = '),
                {
                    'name': "Firewall Status Codes"
                },
                {
                    'name': 'Protocols'
                }
            ],
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    web =  [
        {
            'type': 'checkbox',
            'message': 'Select your options Press Ctrl+C to Exit',
            'name': 'Options',
            'choices': [ 
                Separator('= Type of log ='),
                {
                    'name': 'Type of log'
                },
                Separator('= Exit ='),
                {
                    'name': 'Exit'
                },
                Separator('= IPs ='),
                {
                    'name': 'Most frequently found IPs',
                },
                {
                    'name': 'Least frequently found IPs'
                },
                {
                    'name': 'Number of Unique IPs'
                },
                {
                    'name': 'All of the above'
                },
                Separator('= Status Codes (Web logs) = '),
                {
                    'name': 'Status Codes'
                },
                {
                    'name': 'Count of Request Codes'
                },
                {
                    'name': 'Potentially malicious IPs'
                }
            ],
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    network = [
        {
            'type': 'checkbox',
            'message': 'Select your options Press Ctrl+C to Exit',
            'name': 'Options',
            'choices': [ 
                Separator('= Type of log ='),
                {
                    'name': 'Type of log'
                },
                Separator('= Exit ='),
                {
                    'name': 'Exit'
                },
                Separator('= IPs ='),
                {
                    'name': 'Most frequently found IPs',
                },
                {
                    'name': 'Least frequently found IPs'
                },
                {
                    'name': 'Number of Unique IPs'
                },
                {
                    'name': 'All of the above'
                },
                Separator('= Ports ='),
                {
                    'name': 'Most frequently found ports'
                }
            ],
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    everything = [
        {
            'type': 'checkbox',
            'message': 'Select your options Press Ctrl+C to Exit',
            'name': 'Options',
            'choices': [ 
                Separator('= Type of log ='),
                {
                    'name': 'Type of log'
                },
                Separator('= Exit ='),
                {
                    'name': 'Exit'
                },
                Separator('= IPs ='),
                {
                    'name': 'Most frequently found IPs',
                },
                {
                    'name': 'Least frequently found IPs'
                },
                {
                    'name': 'Number of Unique IPs'
                },
                Separator('= Ports (Network logs)='),
                {
                    'name': 'Most frequently found ports'
                },
                Separator('= Status Codes (Web logs) = '),
                {
                    'name': 'Status Codes'
                },
                {
                    'name': 'Count of Request Codes'
                },
                {
                    'name': 'Potentially malicious IPs'
                },
                Separator('= Status Codes (Firewall logs) = '),
                {
                    'name': "Firewall Status Codes"
                },
                {
                    'name': 'Protocols'
                }
            ],
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    if utility.type_of_log() == 'linux firewall log':
        questions = firewall
    if utility.type_of_log() == 'web server log':
        questions = web
    if utility.type_of_log() == 'network log':
        questions = network
    
    answers = prompt(questions, style=custom_style_2)
    for key, value in answers.items():
        if "Type of log" in value:
            print(utility.type_of_log())
        if "Most frequently found IPs" in value:
            print(utility.print_ip_table(ip_dictionary, True))
        if "Least frequently found IPs" in value:
            print(utility.print_ip_table(ip_dictionary, False))
        if "Number of Unique IPs" in value:
            pprint(utility.unique_ips(ip_set))
        if "All of the above" in value:
            pprint(utility.print_all_ips(ip_dictionary, ip_set))
        if "Most frequently found ports" in value:
            pprint(utility.most_ports(port_dict))
        if "Status Codes" in value:
            pprint(apache.apache_status_code())
        if "Count of Request Codes" in value:
            pprint(apache.apache_request_code())
        if "Potentially malicious IPs" in value:
            pprint(apache.apache_ip_and_code())
        if "Firewall Status Codes" in value:
            pprint(ufw_status.ufw_status_code())
        if "Protocols" in value:
            pprint(ufw_status.ufw_protocol())
        if "Exit" in value:
            return
