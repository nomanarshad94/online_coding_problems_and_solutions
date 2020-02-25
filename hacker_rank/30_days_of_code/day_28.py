#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    l=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        l.append((firstName,emailID))
    result=[i[0] for i in sorted(l,key=lambda x: x[0]) if i[1].endswith('@gmail.com')]
    for i in result:
        print(i)
