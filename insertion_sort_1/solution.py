#!/bin/python3

def insertion_sort(n, arr):
    last = arr[n - 1]
    arr.append(last)
    
    current_index = n - 1
    for i in range(n - 2, -2, -1):
        if last < arr[i]:
            arr[current_index] = arr[i]
            print(" ".join(map(str, arr[:n])))
        else:
            arr[current_index] = last
            print(" ".join(map(str, arr[:n])))
            break
        current_index = i
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertion_sort(n, arr)

