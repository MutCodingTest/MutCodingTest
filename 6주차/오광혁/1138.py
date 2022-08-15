n = int(input())
h = list(map(int,input().split()))
ans = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == h[i] and ans[j] == 0:
            ans[j] = i + 1
            break

        elif ans[j] == 0:
            cnt += 1

for k in ans:
    print(k, end = ' ')