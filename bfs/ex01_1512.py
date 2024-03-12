n = int(input())
x, y = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
result = [[1 for j in range(n)] for i in range(n)]
visited = [[False for l in range(n)] for k in range(n)]


def bfs(i, j):
    queue = []
    visited[i][j] = True
    queue.append([i, j])

    while len(queue) > 0:
        now = queue.pop(0)

        for i in range(4):
            c_x, c_y = now[0] + dx[i], now[1] + dy[i]

            if 0 <= c_x < n and 0 <= c_y < n and not visited[c_x][c_y]:
                visited[c_x][c_y] = True
                result[c_x][c_y] = result[now[0]][now[1]] + 1
                queue.append([c_x, c_y])


bfs(x - 1, y - 1)
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()