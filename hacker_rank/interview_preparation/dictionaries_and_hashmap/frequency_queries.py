#!/bin/python3

import os
from collections import Counter
from collections import defaultdict


# Complete the freqQuery function below.
def freqQuery(queries):
    output = []
    l = defaultdict(int)
    for i in queries:
        if i[0] == 1:
            l[i[1]] += 1
        elif i[0] == 2 and l[i[1]] > 0:
            l[i[1]] -= 1
        elif i[0] == 3:
            if i[1] in l.values():
                output.append(1)
            else:
                output.append(0)
    return output


def freqQuery1(queries):
    d = defaultdict(int)
    output = []
    f = defaultdict(set)

    for (c, v) in queries:
        if c == 3:
            output.append(int(len(f[v]) > 0))
            continue
        f[d[v]].discard(v)
        if c == 1:
            d[v] += 1
        elif d[v] > 0:
            d[v] -= 1
        f[d[v]].add(v)

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
