#!/bin/python3

import math
import os
import random
import re
import sys

def is_leap_year(year):
    if year <= 1917:
        if year % 4 == 0:
            return True
    else:
        if year % 400 == 0:
            return True
        elif year % 4 == 0 and year % 100 != 0:
            return True
    return False

def day_of_programmer(year):
    if year == 1918:
        day = str(41 - 15)
    elif is_leap_year(year):
        day = str(41 - 29)
    else:
        day = str(41 - 28)
    return day + ".09." + str(year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = day_of_programmer(year)

    fptr.write(result + '\n')

    fptr.close()
