# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:40:43 2024

@author: HomePC
"""

"""
data storage in python
1. lists
2. dictionaries
3. data frames - specific to pandas
"""

import pandas
import numpy

file= pandas.read_csv("country_data.csv")


print(file)

"""
    Age Gender       Country
0    39      M  South Africa
1    25      M      Botswana
2    29      F  South Africa
3    46      M  South Africa
4    22      F         Kenya
5    35      F    Mozambique
6    22      F       Lesotho
7    49      M         Kenya
8    30      M         Kenya
9    40      F         Egypt
10   30      M         Sudan
"""

age = [30,25,29,46,22]
#lits can hold all sorts of data types eg float, strings


print(age)

print(age[1])

print(max(age))

print(sum(age))

print(len(age))

print(numpy.average(age))

g1= "m"
g2= "f"
g3="m"

gender= ["M", "F", "M"]
#CREATING LISTS
#alot of values under one variable

print(age[0:5])
#getting a specific number

age.append(100)

print(age)
print(age[0:6])

x= sum(age)
print(x)

age.insert(0,100)  #insert index 
print(age)

"""
Dictionaries - key:value pairs

cat: "a cute animal"

"""

mammals = {"cat":"a cute animal","lion":"king of the jungle",
           "elephant":"a gigantic herbivore"}

print(mammals["cat"])

"""
Data frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]

Size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

fruit_sizes ={
    'fruits': fruits,
    'sizes':Size_nm,
    'prices': prices
    }

#df stands for data frame

import pandas as pd
df = pd.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].describe())

print(df[df["sizes"] > 10])

print(df[1:3])



df['prices'] = prices

df.drop(columns=["sizes"], inplace= True)




















