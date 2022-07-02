n=int(input())
nlist=list(map(int,input().split()))
numlist=[]
finallist=[11]*(n+1)
cnt=1
for i in nlist:
  numlist.append([cnt,i])
  cnt+=1

start=numlist[0][0]
end=numlist[0][1]
finallist[0]=0
finallist[end]=start

for i in range(1,len(numlist)):
  start=numlist[i][0]
  end=numlist[i][1]
  cnt=0
  for j in range(1,len(finallist)):
    if finallist[j]>start:
      cnt+=1
    if cnt==end:
      finallist[j+1]=start
      break
  
print(finallist)