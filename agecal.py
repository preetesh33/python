#!/bin/python


# App to find your age?

m = {
        'jan':1,
        'feb':2,
        'mar':3,
        'apr':4,
        'may':5,
        'jun':6,
        'jul':7,
        'aug':8,
        'sep':9,
        'oct':10,
        'nov':11,
        'dec':12
        }

_yr = int(input("Please year you were born in"))
mn = input("Please month you are born eg dec, jan or feb: ")
cr = input("Please enter current month")
_age = 2019 - _yr

if _age <= 0:
    print("you are not yet born")
elif mn in m:
    if m[mn] > m[cr]:
     a=m[mn] - m[cr]
    elif m[mn] < m[cr]:
     a=m[cr] - m[mn]
    print(f"your current age is {_age}.{a}")
print("Thank you")
