# 백준 1966번 프린터큐

import sys
input = sys.stdin.readline

for _ in range(int(input())):
  n, m = map(int, input().split())
  docs = list(map(int, input().split()))
  doc_number = [i for i in range(len(docs))]
  seq = 0

  while True:
    if docs[0] == max(docs): # 문서를 뺄 때
      now = docs.pop(0)
      num = doc_number.pop(0)
      seq += 1
      if num == m:
        break
    else: # 다시 넣을 때
      now = docs.pop(0)
      docs.append(now)
      num = doc_number.pop(0)
      doc_number.append(num)

  print(seq)