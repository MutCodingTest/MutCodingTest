# # 2206 벽 부수고 이동하기

# from collections import deque
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# graph = []
# visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# for _ in range(n):
#   graph.append(list(map(int, input().rstrip())))

# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# q = deque([(0, 0, 0)])
# distance = set()

# def bfs():
#   while q:
#     x, y, dist, wall = q.popleft()
#     visited[x][y] = 1
#     if x == n-1 and y == m-1:
#       distance.add((dist, wall))
#     for i in range(4):
#       rx = x + dx[i]
#       ry = y + dy[i]
#       if 0 <= rx < n and 0 <= ry < m and not visited[rx][ry]:
#         if graph[rx][ry] == 1:
#           q.append((rx, ry, dist+1, wall+1))
#         else:
#           q.append((rx, ry, dist+1, wall))

# bfs()
# print(distance)

##################

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
q = deque([(0, 0, 0)])
visited[0][0][0] = 1

def bfs():
  while q:
    x, y, z = q.popleft()
    if x == n-1 and y == m-1:
      return visited[x][y][z]
    for i in range(4):
      rx = x + dx[i]
      ry = y + dy[i]
      if 0 <= rx < n and 0 <= ry < m:
        # 두 가지 경우에만 q에 원소 넣고 visited 갱신
        if graph[rx][ry] == 1 and z == 0: # 벽을 깨지 않았고 벽이 있을 경우
          visited[rx][ry][1] = visited[x][y][0] + 1 # 다음 visited[rx][ry][1]
          q.append((rx, ry, 1))
        elif graph[rx][ry] == 0 and not visited[rx][ry][z]: # 벽이 없는 경우
          visited[rx][ry][z] = visited[x][y][z] + 1
          q.append((rx, ry, z)) # z를 넣음으로써 한번 벽을 깨면 [x][y][1]이 증가하게 만듦
  return -1

print(bfs())