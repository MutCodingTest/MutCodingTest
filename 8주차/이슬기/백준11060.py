# 11060번 점프점프

# 8/21 dp 솔

import sys
input = sys.stdin.readline

n = int(input())
miro = list(map(int, input().split()))
dp = [sys.maxsize for _ in range(n)]
dp[0] = 0

for i in range(n-1):
  cnt = miro[i]
  for j in range(cnt):
    try: dp[i+j+1] = min(dp[i+j+1], dp[i]+1)
    except: continue

print(dp[n-1]) if dp[n-1] < sys.maxsize else print(-1)