# for testing python code
from prettytable import PrettyTable
t = PrettyTable(['Name', 'Age'])
t.add_row(['Alice', 24])
t.add_row(['Bob', 19])
t.add_row(['Plamen', 28])
t.add_row(['Haley', 18])
print(t)