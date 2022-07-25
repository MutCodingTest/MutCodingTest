n,k=map(int,input().split())

queue=list()

for i in range(1,n+1):
  queue.append(i)

index=0

ans=[]

for i in range(n):
  index+=k-1
  if index>=len(queue):
    index%=len(queue)
  ans.append(str(queue.pop(index)))

print("<",", ".join(ans),">",sep="")