#!/bin/python3
import os


# Complete the countingValleys function below.
def countingValleys(n, st):
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


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
# Time complexity issue on 3 test cases
