#!/bin/python3

import math
import os


# Complete the repeatedString function below.
# def repeatedString(s, n):

#     count=0
#     for i in s:
#         if i=='a':
#             count+=1
#     # return math.floor(count*n/len(s))

#     return math.ceil(count*n/len(s))
# return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")


def repeatedString(s, n):
    a_cnt = s.count('a')
    num = n // len(s)
    mod = n % len(s)
    print(num)
    print(mod)
    count = a_cnt * num + s[:mod].count('a')
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
