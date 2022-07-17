import copy
n=int(input())
clist=[]
for i in range(n):
  now =list(input())
  clist.append(now)


def check(arr):
  maxcnt=1
  n=len(arr)
  for i in range(n):
    #행체크
    cnt=1
    for j in range(1,n):
      if arr[i][j-1]==arr[i][j]:
        cnt+=1
      else:
        cnt=1
      if cnt>maxcnt:
        maxcnt=cnt
    #열체크
    cnt=1
    for j in range(1,n):
      if arr[j-1][i]==arr[j][i]:
        cnt+=1
      else:
        cnt=1
      if cnt>maxcnt:
        maxcnt=cnt
  return maxcnt

ans=0

for i in range(n):
  for j in range(n):
    if j+1<n:
      clist[i][j],clist[i][j+1]=clist[i][j+1],clist[i][j]
      temp=check(clist)
      if temp>ans:
        ans=temp
      clist[i][j],clist[i][j+1]=clist[i][j+1],clist[i][j]
      
    if i+1<n:
      clist[i][j],clist[i+1][j]=clist[i+1][j],clist[i][j]
      temp=check(clist)
      if temp>ans:
        ans=temp
      clist[i][j],clist[i+1][j]=clist[i+1][j],clist[i][j]

print(ans)