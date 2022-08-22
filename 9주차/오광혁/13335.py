# 트럭

import sys

input = sys.stdin.readline
n,w,l = map(int,input().split()) # n: truck 수/w: 다리의 길이/l: 최대하중
truck = list(map(int,input().split()))
ans = 0
bridge = [0] * w

while bridge:
    ans += 1
    bridge.pop(0)

    if truck: # 남아있는 트럭 확인
        if sum(bridge) + truck[0] <= l: # 다리의 하중보다 작으면 bridge에 추가
            bridge.append(truck.pop(0))

        else: # 다리의 하중보다 크면 빈 공간 추가
            bridge.append(0)

print(ans)