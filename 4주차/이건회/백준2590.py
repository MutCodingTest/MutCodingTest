clist=[]
cnt=0
left5=0
left4=0
left3=0
left2=0
left1=0
for _ in range(6):
  clist.append(int(input()))

#6번 색종이 있으면 그 수만큼 카운트 증가
if clist[5]!=0:
  cnt+=clist[5]
  #6번 색종이 수 0으로
  clist[5]=0

#5번 색종이 있으면 그 수만큼 카운트 증가
if clist[4]!=0:
  cnt+=clist[4]
  #5번 자르고 남은 색종이 수 left5에 저장
  left5=clist[4]
  #남은 5번 색종이 공간(11*남은 5번 색종이 수)
  temp5=11*left5
  #1번색종이가 있으면
  if clist[0]!=0:
    #만약 남은공간이 1번 색종이 수 공간보다 많으면
    if temp5>=clist[0]:
      #1번 색종이 모두 사용
      clist[0]=0
    #만약 1번 색종이 수 공간이 남은공간보다 많으면
    else:
      #1번 색종이를 남은공간만 사용하고 사용한만큼 줄임
      clist[0]-=temp5
      temp5=0
  #5번 색종이 수 0으로
  clist[4]=0

#4번 색종이 있으면 그 수만큼 카운트 증가
if clist[3]!=0:
  cnt+=clist[3]
  #4번 자르고 남은 색종이수 left4에 저장
  left4=clist[3]
  #남은 4번 색종이 공간:
  temp4=20*left4
  #2번색종이가 있으면
  if clist[1]!=0:
    #2번색종이 남은공간
    temp2 = 4*clist[1]
    #만약 남은공간이 2번 색종이 수 공간보다 많으면
    if temp4 >= temp2:
      #2번 색종이 모두 사용
      temp4-=temp2
      clist[1]=0
    #만약 2번 색종이 수 공간이 남은공간보다 많으면
    else:
      #2번 색종이를 남은공간만큼 사용하고 남은공간 0으로
      clist[1] -= left4
      temp4=0
      left4=0
    #만약 남은공간이 있으면
    if temp4 !=0 :
      #만약 1번색종이가 남아있으면
      if clist[0]!=0:
        #남은공간이 1번색종이보다 많으면 1번색종이 다삭제
        if temp4>=clist[0]:
          clist[0]=0
        # 그게아니면 남은공간만큼 1번색종이 삭제
        else:
          clist[0]-=temp4
          temp4=0
  #4번 색종이 수 0으로
  clist[3]=0

#만약 3번색종이 있으면
if clist[2]!=0:
  #4로 나눈 몫+1 만큼 카운트 증가
  cnt += (clist[2]//4)+1
  #만약 4로 딱떨어지면 3번 0으로 초기화하고 다음으로 넘어감
  if clist[2]%4==0:
    clist[2]=0
  else:
    #남은 3번 색종이 공간은 36에서 9*나머지 뺀값
    remain=clist[2]%4
    temp3 = 36-((remain)*9)
    #만약 2번색종이 있으면
    if clist[1]!=0:
      #만약 나머지가 3일때 남은공간에서 4만뺌
      if remain==3:
        temp3-=4
        clist[1]-=1
      #나머지가 2일때
      elif remain==2:
        #남은 2번이 3보다 크거나 같으면 남은공간에서 12뺌
        if clist[1]>=3:
          clist[1]-=3
          temp3-=12 
        #3보다 작으면 4*2번종이만큼 빼고 2번종이 0으로 초기화
        else:
          temp3 -= (clist[1]*4)
          clist[1]=0
      #나머지가 1일 때
      elif remain==1:
        #남은1번이 5보다 크거나 같으면 남은공간에서 20뺌
        if clist[1]>=5:
          clist[1]-=5
          temp3-=20
        #5보다 작으면 4*2번종이만큼 빼고 2번종이 0으로 초기화
        else:
          temp3-=(clist[1]*4)
          clist[1]=0
    #만약 1번색종이 있으면
    if clist[0] != 0:
      #남은색종이가 1번색종이보다 많으면 1번색종이 다삭제
      if temp3>=clist[0]:
        clist[0]=0
      #반대면 1번색종이에서 남은색종이수 삭제
      else:
        clist[0]-=temp3

#만약 2번색종이 있으면
if clist[1]!=0:
  #9로 나눈 몫 +1 만큼 색종이 증가
  cnt+=(clist[1]//9)+1
  #남은공간은 36에서 나머지*4 뺀 값
  remain = clist[1]%9
  temp2= 36 - ((remain)*4)
  #만약 1번색종이 있으면
  if clist[0]!=0:
    #1번색종이 수가 남은공간보다 적으면 1번 0으로 초기화
    if temp2 >= clist[0]:
      clist[0]=0
    #아니면 남은공간만큼 1번 빼줌
    else:
      clist[0]-=temp2

#만약 1번색종이 있으면
if clist[0]!=0:
  #36으로 나눈 몫+1 만큼 색종이 증가
  cnt=(clist[0]//36)+1

print(cnt)