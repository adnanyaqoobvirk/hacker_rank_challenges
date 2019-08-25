#!/bin/python3

import os
import sys

sys.setrecursionlimit(50000)

dp = {}

def memcheck(a, b):
    result = dp.get((a, b), None)
    if result == None:
        result = check(a, b)
        dp[(a, b)] = result
    
    return result

def check(a, b):
    if len(a) == 0 and len(b) == 0:
        return True
    elif len(b) > 0 and len(a) == 0:
        return False
    elif len(a) > 0 and len(b) == 0:
        if a[0].islower():
            return memcheck(a[1:], b)
        else:
            return False
    else:
        if a[0].isupper():
            if a[0] != b[0]:
                return False
            else:
                return memcheck(a[1:], b[1:])
        else:
            return memcheck(a[0].upper() + a[1:], b) or memcheck(a[1:], b)

def abbreviation(a, b):
    return "YES" if check(a, b) else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
