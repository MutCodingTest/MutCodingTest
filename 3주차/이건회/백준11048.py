n,m=map(int,input().split())
clist=[]
for _ in range(n):
  clist.append(list(map(int,input().split())))

for i in range(1,m):
  clist[0][i] += clist[0][i-1]

for i in range(1,n):
  clist[i][0] += clist[i-1][0]

def dp(x,y,m,n):
  for i in range(y,m):
    clist[x][i] += max(
      clist[x-1][i],clist[x][i-1],clist[x-1][i-1]
    )

y=1

for i in range(1,n):
  dp(i,y,m,n)

print(clist[n-1][m-1])