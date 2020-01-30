#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    # BIG O(n*m)
    # for i in range(len(queries)):
    #     for j in range(queries[i][0]-1,queries[i][1]):
    #         arr[j]+=queries[i][2]
    # return max(arr)

    # BIG O(n+m)
    count = 0
    max_ = 0
    for first, last, value in queries:
        arr[first - 1] += value
        arr[last] -= value
        # using array sum algo
    for item in arr:
        count += item
        if count > max_:
            max_ = count

    return max_


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
