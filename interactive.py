from __future__ import print_function, unicode_literals

from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt, Separator

from examples import custom_style_2

from scripts import utility

def interactive():
    questions = [
        {
            'type': 'checkbox',
            'message': 'Select your options',
            'name': 'Options',
            'choices': [ 
                Separator('= Type of log ='),
                {
                    'name': 'Type of log'
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
                Separator('= Ports (network logs)='),
                {
                    'name': 'Most frequently found ports'
                },
                Separator('= Status Codes (firewall logs)= '),
                {
                    'name': 'Request code'
                }
            ],
            'validate': lambda answer: 'You must choose at least one option.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style=custom_style_2)
    for key, value in answers.items():
        if "Type of log" in value:
            pprint(utility.type_of_log())
        if "Most frequently found IPs" in value:
            pprint(utility.most_ips())
        if "Least frequently found IPs" in value:
            pprint(utility.least_ips())
        if "Number of Unique IPs" in value:
            pprint(utility.unique_ips())
        if "Most frequently found ports" in value:
            pprint(utility.most_ports())