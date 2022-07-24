# 9375 패션왕 신해빈

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  clothes = dict()
  for _ in range(int(input())):
    name, kind = input().split()
    if kind in clothes.keys():
      clothes[kind] += 1
    else:
      clothes[kind] = 1
  ans = 1
  for key in clothes:
    ans *= clothes[key]+1
  print(ans-1)
