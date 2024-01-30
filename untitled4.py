# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:25:26 2024

@author: HomePC
"""

import pandas

file4=pandas.read_csv("insurance_data.csv",skiprows=5) #skip no. of rows, csv command only recognizes numbers
print(file4)
print(file4.info())
print(file4.describe())