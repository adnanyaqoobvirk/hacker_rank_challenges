#!/bin/python3

def insertion_sort(n, arr):
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            else:
                break
        print(" ".join(map(str, arr)))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertion_sort(n, arr)
