import sys
from collections import deque
input=sys.stdin.readline

def push(queue,n):
  queue.append(n)

def pop(queue):
  if len(queue)==0:
    print(-1)
  else:
    print(queue.popleft())

def size(queue):
  print(len(queue))

def empty(queue):
  if len(queue)==0:
    print(1)
  else:
    print(0)

def front(queue):
  if len(queue)==0:
    print(-1)
  else:
    print(queue[0])

def back(queue):
  if len(queue)==0:
    print(-1)
  else:
    print(queue[len(queue)-1])

n=int(input())
queue=deque()

for _ in range(n):
  ord=input().split()
  if ord[0]=="push":
    push(queue,ord[1])
  elif ord[0]=="pop":
    pop(queue)
  elif ord[0]=="size":
    size(queue)
  elif ord[0] =="empty":
    empty(queue)
  elif ord[0] == "front":
    front(queue)
  elif ord[0] == "back":
    back(queue)
    