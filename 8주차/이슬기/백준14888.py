# 14888 연산자 끼워넣기

# 옛날엔 못풀었는데,, 백트래킹으로 생각하니까 풀림

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
oper = list(map(int, input().split()))
op_list = []
visited = [0 for _ in range(n-1)]

for op in range(4):
  if op == 0:
    op_list.extend(['+'] * oper[op])
  elif op == 1:
    op_list.extend(['-'] * oper[op])
  elif op == 2:
    op_list.extend(['*'] * oper[op])
  elif op == 3:
    op_list.extend(['/'] * oper[op])

op_value = []

# 계산하기
def calculate(a, b, op):
  a = int(a)
  b = int(b)
  if op == '+':
    return a+b
  elif op == '-':
    return a-b
  elif op == '*':
    return a*b
  elif op == '/':
    if a < 0:
      cal = abs(a) // b
      return -cal
    return a//b

min_value = 1000000000
max_value = -1000000000

# 식 하나당 연산해서 최대, 최소값을 구함
def make_cal(e):
  global min_value, max_value
  i = len(e)//2
  for _ in range(i):
    cal = calculate(e[0], e[2], e[1])
    try:
      e = e[3:]
      e.insert(0, str(cal))
    except:
      e.insert(0, str(cal))
  e = int(e[0])
  min_value = min(e, min_value)
  max_value = max(e, max_value)

# 식 조합하기 (백트래킹)
def make_exp(x, visited):
  if x == n-1:
    i = 0
    st = [str(seq[i])]
    for op in op_value:
      st.append(op)
      i += 1
      st.append(str(seq[i]))
    make_cal(st)
    return
  else:
    for j in range(n-1):
      if not visited[j]:
        visited[j] = 1
        op_value.append(op_list[j])
        make_exp(x+1, visited)
        op_value.pop()
        visited[j] = 0

make_exp(0, visited)

print(max_value)
print(min_value)
