#!/bin/python3

import os
from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    l = []
    output = []
    for i in queries:
        if i[0] == 1:
            l.append(i[1])
        elif i[0] == 2:
            try:
                l.remove(i[1])
            except ValueError:
                pass
        elif i[0] == 3:
            freq1 = Counter(l)
            if i[1] in freq1.values():
                output.append(1)
            else:
                output.append(0)
    return output


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
