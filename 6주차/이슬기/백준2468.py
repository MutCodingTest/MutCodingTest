# 2468번 안전 영역

import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9)

n = int(input())
area = []
for _ in range(n):
  area.append(list(map(int, input().split())))

max_drop = 0
for i in range(n):
  for j in range(n):
    max_drop = max(max_drop, area[i][j])

def make_safe_area(x):
  safe_area = [[1] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if area[i][j] <= x:
        safe_area[i][j] = 0
  return safe_area

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def search_area(safe_area, x, y):
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n:
      if not visited[nx][ny] and safe_area[nx][ny] == 1:
        search_area(safe_area, nx, ny)
  return True

ans = 0
for drop in range(max_drop+1): # 빗물이 높이가 1인 경우도 주의
  safe_area = make_safe_area(drop)
  visited = [[0] * n for _ in range(n)]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if safe_area[i][j] == 1 and not visited[i][j]:
        if search_area(safe_area, i, j) == True:
          cnt += 1
  ans = max(cnt, ans)
print(ans)