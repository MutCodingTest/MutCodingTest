# 1244번 스위치 켜고 끄기

import sys
input = sys.stdin.readline

n = int(input())
swh = [0] + list(map(int, input().split()))

def male(x):
  global n
  t = 1
  w = x
  while w <= n:
    swh[w] = 0 if swh[w] == 1 else 1
    t += 1
    w = x * t

def female(x):
  global n
  swh[x] = 0 if swh[x] == 1 else 1
  t = 1
  while True:
    if x-t > 0 and x+t <= n:
      if swh[x-t] == swh[x+t]:
        swh[x-t] = 0 if swh[x-t] == 1 else 1
        swh[x+t] = 0 if swh[x+t] == 1 else 1
        t += 1
      else:
        break
    else:
      break

for _ in range(int(input())):
  sex, num = map(int, input().split())
  if sex == 1:
    male(num)
  else:
    female(num)

cnt = 0
for s in range(1, n+1):
  if cnt % 20 == 0 and cnt != 0:
    print()
  print(swh[s], end=' ')
  cnt += 1
