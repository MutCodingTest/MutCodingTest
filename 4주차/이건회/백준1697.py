from collections import deque
n,k=map(int,input().split())
visited = [0]*(200000)

def bfs(start,end,visited):
  if end<start:
    visited[end]=start-end
    return
  if start == end:
    visited[end]=0
    return
  if abs(start-end)==1 or ((int(start/2)==end) or int(end/2)==start):
    visited[end]=1
    return
  queue=deque([start])
  visited[start]=0
  v = queue.popleft()
  visited[v-1]=1
  queue.append(v-1)
  visited[v+1]=1
  queue.append(v+1)
  visited[v*2]=1
  queue.append(v*2) 
  
  while queue:
    v=queue.popleft()   
    for i in (v-1,v+1,v*2):
      if 0<=i<=k+1:
        if visited[i]==0 and i != start:
          visited[i]= visited[v]+1
          queue.append(i)
        else:
          if visited[i]>visited[v]+1:
            visited[i]=visited[v]+1
            queue.append(i)
    if v==end:
      break
    

bfs(n,k,visited)
print(visited[k])