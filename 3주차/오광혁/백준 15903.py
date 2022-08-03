# 키드 합체 놀이/그리디

''' Sol.1 '''
import sys

input = sys.stdin.readline
n,m = map(int,input().split())

card = list(map(int,input().split()))

for _ in range(m):
    card.sort()
    tmp = card[0] + card[1]
    card[0] = tmp
    card[1] = tmp

print(sum(card))