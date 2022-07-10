# 14502번 연구소

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lab = [] # 초기 맵
walls = [[0]*m for _ in range(n)]

for i in range(n):
  lab.append(list(map(int, input().split())))

ans = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def defuse(x, y):
  global n, m
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if walls[nx][ny] == 0:
        walls[nx][ny] = 2
        defuse(nx, ny)

def get_virus():
  virus = 0
  for i in range(n):
    for j in range(m):
      if walls[i][j] == 0:
        virus += 1
  return virus

def dfs(cnt):
  global ans
  if cnt == 3: # 백트래킹
    for i in range(n):
      for j in range(m):
        walls[i][j] = lab[i][j] # walls를 모두 완성하고 난 뒤
    for i in range(n):
      for j in range(m):
        if walls[i][j] == 2:
          defuse(i, j)
    ans = max(ans, get_virus())
    return
  for i in range(n): 
    for j in range(m):
      if lab[i][j] == 0:
        lab[i][j] = 1
        cnt += 1
        dfs(cnt)
        lab[i][j] = 0
        cnt -= 1

dfs(0)
print(ans)