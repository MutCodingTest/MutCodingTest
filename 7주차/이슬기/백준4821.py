# 페이지 세기

import sys
input = sys.stdin.readline

while True:
  n = int(input())
  if n == 0:
    break
  page = [0] * (n+1)
  print_pages = input().split(",")

  for p in print_pages:
    bundle = p.split("-")
    if len(bundle) == 2:
      low, high = int(bundle[0]), int(bundle[1])
      for i in range(low, high+1):
        try: page[i] = 1
        except: continue
    else:
      num = int(bundle[0])
      try : page[num] = 1
      except: continue

  print(page.count(1))