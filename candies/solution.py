#!/bin/python3

import math
import os
import random
import re
import sys

def candies(n, arr):
    candies_list = []
    score = 1
    for i in range(n):
        if i == 0:
            candies_list.append(score)
        else:
            if arr[i - 1] < arr[i]:
                score += 1
                candies_list.append(score)
            else:
                score = 1
                candies_list.append(score)

    total_candies = 0
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1] and candies_list[i] >= candies_list[i - 1]:
            candies_list[i - 1] = candies_list[i] + 1
        total_candies += candies_list[i]
    total_candies += candies_list[0]
    
    return total_candies

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
