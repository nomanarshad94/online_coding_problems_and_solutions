#!/bin/python3

import os


# Complete the minimumBribes function below.
# Others solution
# def minimumBribes1(q):
#     bribe = 0
#     for i in range(len(q)-1,-1,-1):
#         if q[i] - (i + 1) > 2:
#             print('Too chaotic')
#             return
#         for j in range(max(0, q[i] - 2),i):
#             if q[j] > q[i]:
#                 bribe+=1
#     print(bribe)

def minimumBribes(queue):
    lastIndex = len(queue) - 1
    bribe = 0
    swaped = False
    # check if the queue is too chaotic
    for i, v in enumerate(queue):
        if (v - 1) - i > 2:
            print("Too chaotic")
            return
    # bubble sorting to find the answer
    for i in range(0, lastIndex):
        for j in range(0, lastIndex):
            if queue[j] > queue[j + 1]:
                queue[j], queue[j + 1] = queue[j + 1], queue[j]
                bribe += 1
                swaped = True
        # In case of 0 bribes on single scaning of array then  return
        if swaped:
            swaped = False
        else:
            break
    print(bribe)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
