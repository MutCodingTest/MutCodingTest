# 다리 놓기

def facto(x):
    res = 1
    for i in range(1,x+1):
        res *= i

    return res

t = int(input())

for _ in range(t):
    n,m = map(int,input().split()) # n <= m
    print(facto(m) // (facto(n) * facto(m-n))) # mCn 조합으로 해결