from collections import deque


n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append([int(char) for char in input()])


def process(board: list):
    visited = [[False] * len(board[0]) for _ in range(len(board))]

    def bfs():
        # visited[0][0] = True
        q = deque()
        q.append((0, 0, 1))
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while q:
            x, y, _level = q.popleft()
            if (x, y) == (len(board) - 1, len(board[0]) - 1):
                return _level
            for i in range(len(dx)):
                adj_x, adj_y = x + dx[i], y + dy[i]
                # out of index
                if adj_x < 0 or adj_y < 0 or adj_x >= len(board) or adj_y >= len(board[0]):
                    continue
                # already visited or 0
                if visited[adj_x][adj_y] or (board[adj_x][adj_y] != 1):
                    continue
                visited[adj_x][adj_y] = True
                q.append((adj_x, adj_y, _level + 1))

    result = bfs()
    print(result)


process(board)
