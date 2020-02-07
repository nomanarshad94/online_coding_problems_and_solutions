#!/bin/python3

def hourglassSum(arr):
    rows = len(arr)
    cols = len(arr[0])
    maxi = -9 * 7
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            s = sum([arr[r - 1][c - 1], arr[r - 1][c + 1], arr[r - 1][c],
                     arr[r][c],
                     arr[r + 1][c - 1], arr[r + 1][c + 1], arr[r + 1][c]])
            if s > maxi:
                maxi = s
    return maxi


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))
