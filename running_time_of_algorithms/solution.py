#!/bin/python3

import os

def running_time(n, arr):
    shifts = 0
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
                shifts += 1
            else:
                break
    return shifts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = running_time(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
