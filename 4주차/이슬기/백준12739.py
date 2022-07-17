# 12739번 돌림판(Small)

import sys, copy
input = sys.stdin.readline

n, k = map(int, input().split())
wheel = list(input().rstrip())
t_wheel = copy.copy(wheel)

def count_color(x):
  kind = [0, 0, 0]
  for i in range(-1, 2):
    y = x + i
    if i == 1 and x == n-1:
      y = 0
    if t_wheel[y] == 'R':
      kind[0] += 1
    elif t_wheel[y] == 'G':
      kind[1] += 1
    elif t_wheel[y] == 'B':
      kind[2] += 1
  return kind

def change_color(x):
  global wheel
  kind = count_color(x)
  if kind[0] == 1 and kind[1] == 1:
    wheel[x] = 'B'
  elif 3 in kind:
    wheel[x] = 'B'
  elif kind[0] == 2 and kind[1] == 1:
    wheel[x] = 'R'
  elif kind[1] == 2 and kind[2] == 1:
    wheel[x] = 'R'
  elif kind[2] == 2 and kind[0] == 1:
    wheel[x] = 'R'
  else:
    wheel[x] = 'G'

for t in range(k):
  for i in range(n):
    change_color(i)
  t_wheel = copy.copy(wheel)

ans = [0, 0, 0]
for w in wheel:
  if w == 'R':
    ans[0] += 1
  elif w == 'G':
    ans[1] += 1
  elif w == 'B':
    ans[2] += 1

for a in ans:
  print(a, end=' ')