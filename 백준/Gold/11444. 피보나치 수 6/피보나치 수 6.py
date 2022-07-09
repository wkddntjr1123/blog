from sys import stdin

input = stdin.readline

n = int(input())
base_matrix = [[1, 1], [1, 0]]

# 두 행렬 곱한 행렬 리턴
def matrix_mul(A, B):
    res = [
        [A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
        [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]],
    ]
    for i in range(2):
        for j in range(2):
            res[i][j] %= 1000000007
    return res


def process(x):
    if x == 1:
        return base_matrix
    half = process(x // 2)
    if x % 2 == 0:
        return matrix_mul(half, half)
    else:
        return matrix_mul(matrix_mul(half, half), base_matrix)


print(process(n)[0][1])