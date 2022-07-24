# 5525번 IOIOI

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()
p_string = ''
ioi_n = 'I' + 'OI' * n
cnt = 0

for i in s:
  if p_string == ioi_n:
    cnt += 1
    p_string = p_string[2:]
  if i == 'I':
    if p_string == '':
      p_string += 'I'
    else:
      if p_string[-1] == 'O':
        p_string += 'I'
      else:
        p_string = 'I'
  elif p_string != '' and i == 'O':
    if p_string[-1] == 'I':
      p_string += 'O'
    elif p_string[-1] == 'O':
      p_string = ''
  else:
    p_string = ''

print(cnt)