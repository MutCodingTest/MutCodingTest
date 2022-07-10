graph=[]

for _ in range(5):
  inputs=list(map(str,input().split()))
  graph.append(inputs)

# numlist=[]
numlist=set()

dx=[0,0,1,-1]
dy=[1,-1,0,0]


def dfs(x,y,num):
  if len(num)==6:
    numlist.add(num)
    return -1
  if (x<0 or x>=5) or (y<0 or y>=5):
    return -1
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if 0<=nx<5 and 0<=ny<5:
      dfs(nx,ny,num+graph[nx][ny])

for i in range(5):
  for j in range(5):
    dfs(i,j,graph[i][j])

print(len(numlist))
    
    
  