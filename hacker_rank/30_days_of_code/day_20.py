#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))


# Write Your Code Here
def countSwaps(a):
    c = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                c += 1

    print("Array is sorted in", c, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])


countSwaps(a)