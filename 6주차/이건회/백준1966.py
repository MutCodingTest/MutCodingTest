import heapq
from collections import deque
import sys
input= sys.stdin.readline

t=int(input())

for _ in range(t):
  n,m=map(int,input().split())
  nums=list(map(int,input().split()))
  numlist=[]
  target=nums[m]
  for i in range(len(nums)):
    if i==m:
      numlist.append((nums[i],1))
    else:
      numlist.append((nums[i],0))
  
  queue=deque()
  for num in numlist:
    queue.append(num)
  # print(queue)
  
  stack=[]
  while queue:
    if queue[0][0]<max(queue)[0]:
      a=queue.popleft()
      queue.append(a)
      # print(queue)
    else:
      a=queue.popleft()
      stack.append(a)
      # print(queue)
      # print(stack)
  
  
  for i in range(len(stack)):
    if stack[i][1]==1:
      print(i+1)