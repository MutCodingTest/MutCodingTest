import copy

a=int(input())
cnt=1
total=0
numlist=[]
while True:
  numlist.append(list(range(1,cnt+1)))
  total+=cnt
  cnt+=1
  if total>a:
    break

print(numlist)

cnt2=0
for nums in numlist:
  for num in nums:
    cnt2 += 1
    if cnt2 % 2 ==0:
      numss=reversed(nums)
    else:
      numss=list(nums.copy())
    if cnt2 == a:
      target=numss
      targetpoint=num
      break

print(target)
print(targetpoint)
if cnt2 % 2==1:
  print()