# 퇴사 2

import sys

input = sys.stdin.readline
n = int(input())

dp = [0] * (n+1)
t = []
p = []

for _ in range(n):
    a,b = list(map(int,input().split()))
    t.append(a)
    p.append(b)

for i in range(n-1,-1,-1): # 뒤에서부터 확인
    if t[i] + i > n: # 주어진 시간을 넘어갔을 때
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1])

print(dp[0])