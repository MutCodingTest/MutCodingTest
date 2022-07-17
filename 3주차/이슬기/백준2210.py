# 2210번 숫자판 점프

from collections import deque
import sys
input = sys.stdin.readline

graph = []
for _ in range(5):
  graph.append(list(map(int, input().split())))

digit = set()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(x, y):
  q = deque([(str(graph[x][y]), x, y, 0)])
  while q:
    now, a, b, cnt = q.popleft()
    if cnt == 5:
      digit.add(now)
    elif cnt > 5:
      break
    for i in range(4):
      rx = a + dx[i]
      ry = b + dy[i]
      if 0 <= rx < 5 and 0 <= ry < 5:
        st = now + str(graph[rx][ry])
        q.append((st, rx, ry, cnt+1))

for i in range(5):
  for j in range(5):
    bfs(i, j)

print(len(digit))