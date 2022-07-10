# 11051번 이항계수2

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[1] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
  for j in range(1, k+1):
    if i == j:
      dp[i][j] = 1
    elif j == 1:
      dp[i][j] = i
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k] % 10007)