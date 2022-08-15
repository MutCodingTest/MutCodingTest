# 2217번 로프

import sys
input = sys.stdin.readline

n = int(input())
lopes = [int(input()) for _ in range(n)]
lopes.sort(reverse=True)
max_value = 0

for i in range(n):
  lopes[i] *= (i+1)
  max_value = max(lopes[i], max_value)

print(max_value)
