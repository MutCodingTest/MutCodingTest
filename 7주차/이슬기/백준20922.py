# 20922번 겹치는 건 싫어

# 처음엔 리스트로 풀려고 시도

# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())
# seq = list(map(int, input().split()))
# cnt = [0] * 100001 # cnt로 개수를 표시

# left = 0
# right = 1
# over_list = [seq[0]]
# cnt[seq[0]] = 1
# ans = 1

# while right < n and left < right:
#   cnt[seq[right]] += 1
#   if cnt[seq[right]] > k:
#     cnt[seq[left]] -= 1
#     over_list.pop(0)
#     left += 1
#     cnt[seq[right]] -= 1
#   else:
#     over_list.append(seq[right])
#     right += 1
#   ans = max(len(over_list), ans)

# print(ans)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

left = 0
right = 0
over_list = {}
ans = 0

while right < n:
  cnt = over_list.get(seq[right], 0) # seq[right]의 값을 가져옴, 없으면 0
  if cnt < k:
    over_list[seq[right]] = over_list.get(seq[right], 0) + 1
    right += 1
  else:
    over_list[seq[left]] = over_list.get(seq[left], 0) - 1
    left += 1
  ans = max(ans, right-left)

print(ans)
