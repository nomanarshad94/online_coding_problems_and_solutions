#!/bin/python3

from collections import Counter


# Complete the checkMagazine function below.

# two test cases timeout
def checkMagazine1(magazine, note):
    for j in range(len(note)):
        flag = False
        if note[j] in magazine:
            magazine.remove(note[j])
            flag = True
        else:
            break
    if flag:
        print('Yes')
    else:
        print('No')


# optimized
def checkMagazine(magazine, note):
    if not (Counter(note) - Counter(magazine)):
        print('Yes')
        return
    print('No')


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
