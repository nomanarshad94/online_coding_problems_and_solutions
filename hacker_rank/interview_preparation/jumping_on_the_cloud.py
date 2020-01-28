#!/bin/python3

import os


# few test cases failed
# def jumpingOnClouds(c):
# jumps=len(c)-1
# cons_zeros=0
# for i,v in enumerate(c):
#     if v ==1:
#         jumps-=1
#         cons_zeros=0
#     else:
#         cons_zeros+=1
#         if cons_zeros%3==0:
#             jumps-=1
# return jumps
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps, i = 0, 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i + 2] != 1:
            i += 1
        jumps += 1
        i += 1
    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
