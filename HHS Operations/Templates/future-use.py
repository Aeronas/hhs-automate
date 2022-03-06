# !Python3                                              A3R0NA$
from tkinter import *
import openpyxl as op
from copy import copy
'''Future use codes for updates'''


# Checking if month sheet exists or creating it
if month_name in proj_wb.sheetnames:
    proj_ws = proj_wb[month_name]
else:
    proj_ws = proj_wb.add_sheet[month_name]
    # TODO Copy tracking template onto new sheet
