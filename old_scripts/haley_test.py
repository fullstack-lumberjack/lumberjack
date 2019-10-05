#!/usr/bin/env python3
import sys
from easy_table import EasyTable

myTable = EasyTable

myTable.setTableCorners("/", "\\", "/", "\\")
myTable.setTableBorder("|", "-")
myTable.setTableInnerStructure("|", "-", "+")

myTable.setColumns(["ID #", "Name", "Age"])
data = [["0","Jeff","31"],["1","Bill", "22"], ["2", "Tim", "33"], ["3", "Timothy", "41"]]
myTable.setData(data)

myTable.displayTable()