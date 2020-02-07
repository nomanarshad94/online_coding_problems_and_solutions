#!/bin/python3

import math
import os
from collections import defaultdict


# Complete the countTriplets function below.
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1
    return count


# def countTriplets(arr, r):
#     # stores number of tuples with two elements that can be formed if we find the key
#     potential_two_tuples = defaultdict(int)
#     # stores number of tuples with three elements that can be formed if we find the key
#     potential_three_tuples = defaultdict(int)
#     count = 0
#     for k in arr:
#         # k completes the three tuples given we have already found k/(r^2) and k/r
#         count += potential_three_tuples[k]
#         # For any element of array we can form three element tuples if we find k*r given k / r is already found. Also k forms the second element.
#         potential_three_tuples[k*r] += potential_two_tuples[k]
#         # For any element of array we can form two element tuples if we find k*r. Also k forms the first element.
#         potential_two_tuples[k*r] += 1
#     return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
