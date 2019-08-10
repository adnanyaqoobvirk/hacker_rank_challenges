#!/bin/python3

import math
import os
import random
import re
import sys

def forming_magic_square(s):
    valid_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]], 
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]], 
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]], 
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
    ]
    
    min_cost = sys.maxsize
    for magic_square in valid_magic_squares:
        cost = 0
        for i in range(3):
            cost += abs(magic_square[i][0] - s[i][0])
            cost += abs(magic_square[i][1] - s[i][1])
            cost += abs(magic_square[i][2] - s[i][2])
        if cost < min_cost:
            min_cost = cost
    return min_cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = forming_magic_square(s)

    fptr.write(str(result) + '\n')

    fptr.close()
