from collections import deque
from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]  # 레벨 계산을 그냥 visitied로만 해도 됨

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def valid_index(x, y):
    global n, m
    return 0 <= x < n and 0 <= y < m


def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y, 0))
    visited[start_x][start_y][0] = 1
    while q:
        x, y, meet_wall = q.popleft()  # 이전에 벽을 통과 했으면 meet_wall == 1
        if x == n - 1 and y == m - 1:  # 끝에 도착
            return visited[x][y][meet_wall]
        for i in range(4):
            adj_x, adj_y = x + dx[i], y + dy[i]
            if valid_index(adj_x, adj_y) and not visited[adj_x][adj_y][meet_wall]:
                if board[adj_x][adj_y] == 0:  # 0이면 이전에 벽을 통과했든 안했든 가능
                    q.append((adj_x, adj_y, meet_wall))
                    visited[adj_x][adj_y][meet_wall] = visited[x][y][meet_wall] + 1
                else:
                    if not meet_wall:  # 1이면 이전에 벽을 통과 했으면 불가능
                        q.append((adj_x, adj_y, 1))
                        visited[adj_x][adj_y][1] = visited[x][y][meet_wall] + 1
    return -1  # 끝에 도착 X


result = bfs(0, 0)
print(result)