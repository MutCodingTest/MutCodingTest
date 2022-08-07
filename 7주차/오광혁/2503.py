# 숫자 야구

from itertools import permutations

n_list = list(permutations([1,2,3,4,5,6,7,8,9],3))

q = int(input())

for _ in range(q):
    num, s, b = map(int,input().split())
    num = list(str(num))
    cnt = 0

    for i in range(len(n_list)):
        s_cnt = 0
        b_cnt = 0
        i -= cnt
        
        for j in range(3):
            if n_list[i][j] == int(num[j]): # n_list의 자리수와 num의 자리수가 같을 때
                s_cnt += 1
            elif int(num[j]) in n_list[i]: # num의 자리수가 n_list 안에 있을 때
                b_cnt += 1
        
        if s_cnt != s or b_cnt != b:
            n_list.remove(n_list[i])
            cnt += 1

print(len(n_list))