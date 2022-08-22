# 14716번 현수막

# 기본적인 dfs문제

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

def dfs(x, y):
  visited[x][y] = 1
  for i in range(8):
    rx = dx[i] + x
    ry = dy[i] + y
    if 0 <= rx < n and 0 <= ry < m:
      if not visited[rx][ry] and graph[rx][ry] == 1:
        dfs(rx, ry)

ans = 0
for i in range(n):
  for j in range(m):
    if not visited[i][j] and graph[i][j] == 1:
      dfs(i, j)
      ans += 1

print(ans)