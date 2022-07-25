# 10973번 이전 순열

# 백트래킹으로 풀어봄
# 시간초과 남

# import sys, copy
# input = sys.stdin.readline

# sys.setrecursionlimit(10**9)

# n = int(input())
# arr = [0] * n
# visited = [0 for _ in range(n+1)]
# tup = [i for i in range(1, n+1)]
# st = list(map(int, input().split()))
# ans = []

# def dfs(x):
#   if x == n:
#     if arr == st:
#       if ans:
#         print(*ans)
#       else:
#         print(-1)
#       return
#     temp = copy.copy(arr)
#     if ans:
#       ans.pop()
#     ans.append(temp)
#   else:
#     for j in range(n):
#       if not visited[j]:
#         visited[j] = 1
#         arr[x] = tup[j]
#         dfs(x+1)
#         arr[x] = 0
#         visited[j] = 0

# dfs(0)

# 순열 라이브러리 사용해서 풀어봄
# 메모리 초과 남..

# import itertools, sys
# input = sys.stdin.readline

# n = int(input())
# st = tuple(map(int, input().split()))
# arr = [i for i in range(1, n+1)]
# num_list = list(itertools.permutations(arr, n))

# for i in range(len((num_list))):
#   if num_list[i] == st:
#     print(*num_list[i-1])
#     sys.exit(0)
# print(-1)

import sys
input = sys.stdin.readline

n = int(input())
st = list(map(int, input().split()))

for i in range(n-1, 0, -1):
  if st[i] < st[i-1]:
    for j in range(n-1, 0, -1):
      if st[j] < st[i-1]:
        st[j], st[i-1] = st[i-1], st[j]
        st = st[:i] + sorted(st[i:], reverse=True)
        print(*st)
        sys.exit(0)
print(-1)