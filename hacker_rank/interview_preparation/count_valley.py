#!/bin/python3
import os


# Complete the countingValleys function below.
# Time complexity issue on 3 test cases using this approach
def counting_valleys_naive_approach(n, st):
    valley = [0]

    for s in st:
        if s == 'D':
            if len(valley) == 1:
                valley[0] = valley[0] + 1
                valley.append(s)

            else:
                try:
                    valley.remove('U')
                except ValueError:
                    valley.append('D')
        elif s == 'U':
            if len(valley) > 1:
                try:
                    valley.remove('D')
                except ValueError:
                    valley.append('U')
            else:
                valley.append('U')
    return valley[0]


# optimized approach
def countingValleys(n, s):
    level = valley = 0
    for i in range(n):
        if s[i] == 'U':
            level += 1
            if level == 0:
                valley += 1
        else:
            level -= 1

    return valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
