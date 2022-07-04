n=int(input()) #스위치수
slist=list(map(int,input().split())) #스위치 상태
slist.insert(0,100)
stunum=int(input()) #학생수
students=[]
for _ in range(stunum):
  x,y= map(int,input().split())
  students.append([x,y])

# print("slist",slist)
# print("students",students)

for x,y in students:
  # print("x,y :",x,y)
  if x==1: #남
    for i in range(y,len(slist)): #y에서 끝까지
      if i % y !=0: #y의 배수가 아니면 넘어감
        continue
      else: #y배수면 0->1, 1->0
        if slist[i]==1:
          slist[i]=0
        else:
          slist[i]=1
      
  else:#x==2 여
    if slist[y]==1:
          slist[y]=0
    else:
      slist[y]=1
    if y==1: #y가 1이면 대칭이 불가하므로 그냥 바꾸고 탈출
        # print(slist[1:],"slist")
        continue
    if y==len(slist)-1: #y가 맨 끝이면 역시 대칭 불가하므로 바꾸고 탈출
      # print(slist[1:],"slist")
      continue
    left=y-1
    right=y+1
    while True:
      # print(left,right)
      if slist[left]==slist[right]: #양쪽이 같으면 바꿈
        if (slist[left]==1) and (slist[right]==1):
          slist[left]=0
          slist[right]=0
        else:
          slist[left]=1
          slist[right]=1

        left-=1
        right+=1
        if left<1 or right>(len(slist)-1):
          break
      else: #안같으면 반복문 탈출
        break
  # print(slist[1:],"slist")


for i in range(1,len(slist)):
  if i%20==0:
    print(slist[i])
  else:
    print(slist[i],end=" ")
        
        
  