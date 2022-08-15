# 전깃줄

n = int(input())
elec = []
dp = [1] * n

for _ in range(n):
    elec.append(list(map(int,input().split())))
elec.sort()

for i in range(n):
    for j in range(i):
        if elec[i][1] > elec[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))