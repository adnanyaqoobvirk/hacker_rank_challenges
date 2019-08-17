#!/bin/python3

import math
import os
import random
import re
import sys

def get_connected_cities(n, edges):
    city_map = {i:i for i in range(1, n+1)}
    set_map = {i:[i] for i in range(1, n+1)}
    for u,v in edges:
        if city_map[u] != city_map[v]:
            temp = city_map[v]
            for i in set_map[city_map[v]]:
                city_map[i] = city_map[u]
                set_map[city_map[u]].append(i)
            del set_map[temp]
            
    return set_map.values()

def roads_and_libraries(n, c_lib, c_road, cities):
    connected_cities = get_connected_cities(n, cities)
    total_cost = 0
    for s in connected_cities:
        if c_lib > c_road:
            total_cost += c_lib + ((len(s) - 1) * c_road)
        elif c_road > c_lib:
            total_cost += c_lib * len(s)
        else:
            total_cost += c_road * (len(s) - 1)
            
    return total_cost
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roads_and_libraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
