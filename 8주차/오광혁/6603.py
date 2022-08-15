# 로또

from itertools import combinations

while True:
    n = list(map(int,input().split()))

    if n[0] == 0:
        exit()
    else:
        lotto = n[1:]
        ans = list(combinations(lotto,6))

        for i in ans:
            for j in i:
                print(j, end = " ")
            print()
        print()