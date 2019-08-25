#!/bin/python3

import os

def abbreviation(a, b):
    dp = [[False for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    dp[0][0] = True
    
    has_upper = False
    for i in range(1, len(a) + 1):
        dp[i][0] = True
        if a[i - 1].isupper() or has_upper:
            has_upper = True
            dp[i][0] = False

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            elif a[i - 1].isupper():
                dp[i][j] = False
            elif a[i - 1].upper() == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return "YES" if dp[len(a)][len(b)] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()
