#!/bin/python3
import os


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    odd=[]
    even=[]
    for i in range(len(ar)):
        item=ar[i]
        if item in odd:
            even.append(odd.remove(item))
        else:
            odd.append(item)
    return len(even)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
