import sys
from import_test import Haley, Lance

# print(import_test)
Haley.import_plamen()
Lance.import_plamen()
# def ufw_test():
#     return "this is ufw"

def switch(arg):
    switcher = {
        "ufw": ufw_test(),
        "apache": "this is apache"
    }
    print(switcher.get(arg, "invalid log"))

switch("ufw")

