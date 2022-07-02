import sys
sys.setrecursionlimit(5000)
input = sys.stdin.readline

n,m = map(int,input().split())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def dfs(graph,v):
  visited[v]=True
  for i in graph[v]:
    if visited[i] != True:
      dfs(graph,i)

cnt=0
for i in range(1,n+1):
  if not visited[i]:
    dfs(graph,i)
    cnt+=1
print(cnt)