from collections import deque

n,m=map(int,input().split())
graph=[]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
for i in range(n):
  nums=list(map(int,input().split()))
  graph.append(nums)



def dfs(x,y,graph):
  if x<0 or x>=n or y<0 or y>=m:
    return False
  if graph[x][y]==2:
    if 0<=x+1<n and 0<=y<m:
      if graph[x+1][y]==0:
        graph[x+1][y]=2
        dfs(x+1,y,graph)
    if 0<=x<n and 0<=y+1<m:
      if graph[x][y+1]==0:
        graph[x][y+1]=2
        dfs(x,y+1,graph)
    if 0<=x-1<n and 0<=y<m:
      if graph[x-1][y]==0:
        graph[x-1][y]=2
        dfs(x-1,y,graph)
    if 0<=x<n and 0<=y-1<m:
      if graph[x][y-1]==0:
        graph[x][y-1]=2
        dfs(x,y-1,graph)
    return True
  return False

for i in range(n):
  for j in range(m):
    dfs(i,j,graph)

for i in graph:
  print(i)
  print()
