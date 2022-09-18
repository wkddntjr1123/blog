from sys import stdin

input = stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def getAscTable(arr):
    table = [1 for _ in range(n)]
    for i in range(1, len(arr)):
        maxVal = 0
        for j in range(i):
            if arr[j] < arr[i]:
                maxVal = max(maxVal, table[j])
        table[i] = maxVal + 1
    return table


table = getAscTable(arr)
arr.reverse()
reverseTable = getAscTable(arr)
reverseTable.reverse()

answer = 0
for i in range(n):
    answer = max(answer, table[i] + reverseTable[i] - 1)
print(answer)
