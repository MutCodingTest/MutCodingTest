# 2578번 빙고

import sys
input = sys.stdin.readline

bingo_pan = []
is_talked = [[0] * 5 for _ in range(5)]
num = [] # 사회자가 부르는 수
count = 0
for _ in range(5):
  bingo_pan.append(list(map(int, input().split())))

for _ in range(5):
  num.append(list(map(int, input().split())))

def bingo(x):
  cnt = 0
  for u in range(5):
    if x[u][0] == 1 and x[u][1] == 1 and x[u][2] == 1 and x[u][3] == 1 and x[u][4] == 1:
      cnt += 1
    if  x[0][u] == 1 and x[1][u] == 1 and x[2][u] == 1 and x[3][u] == 1 and x[4][u] == 1:
      cnt += 1
  if x[0][0] == 1 and x[1][1] == 1 and x[2][2] == 1 and x[3][3] == 1 and x[4][4] == 1:
    cnt += 1
  if x[0][4] == 1 and x[1][3] == 1 and x[2][2] == 1 and x[3][1] == 1 and x[4][0] == 1:
    cnt += 1
  return cnt

for i in range(5):
  for j in range(5):
    m = num[i][j]
    count += 1
    for k in range(5):
      if bingo_pan[k].count(m) > 0:
        idx = bingo_pan[k].index(m)
        is_talked[k][idx] = 1
        break
    if bingo(is_talked) >= 3: # 빙고가 3개 이상일 경우
      print(count)
      sys.exit(0)

