import sys
from collections import defaultdict

input=sys.stdin.readline


t=int(input())
for _ in range(t):
  n=int(input())
  clothes=defaultdict(list)
  type=set()
  
  for _ in range(n):
    a,b=map(str,input().split())
    clothes[b].append(a)
    type.add(b)
  
  type=list(type)
  cnt=1
  
  for i in type:
    cnt *= len(clothes[i])+1
  
  print(cnt-1)