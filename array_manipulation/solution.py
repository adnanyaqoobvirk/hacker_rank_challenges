#!/bin/python3

import os

def array_manipulation(n, queries):
    arr = [0] * (n + 1)
    for start_index, end_index, value in queries:
        arr[start_index - 1] += value
        arr[end_index] -= value
    
    max_value = 0
    total = 0
    for i in range(n + 1):
        total += arr[i]
        if total > max_value:
            max_value = total

    return max_value

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = array_manipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
