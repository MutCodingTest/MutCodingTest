import sys
from collections import deque
input = sys.stdin.readline

m,n = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dx = [0,0,-1,1]
dy = [1,-1,0,0]
queue = deque([])

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            queue.append([i,j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] ==0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

bfs()

print(graph)
