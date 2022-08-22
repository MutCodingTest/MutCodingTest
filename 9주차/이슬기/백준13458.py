# 13458번 시험 감독

import sys
input = sys.stdin.readline

n = int(input())
test = map(int, input().split())
b, c = map(int, input().split())
ans = 0

for t in test:
  de = t - b
  if de > 0:
    remain = de % c
    if remain == 0:
      m = de // c
      ans += (m+1)
    else:
      m = de // c
      ans += (m+2)
  else:
    ans += 1

print(ans)
