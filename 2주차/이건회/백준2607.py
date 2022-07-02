n=int(input())
word=input()
total=0 # 최종 갯수
for _ in range(n-1):
  word2=input()
  cnt1=0 
  cnt2=0#바뀌어야 하는 갯수

  if len(word2)>len(word)+1:
    continue

  if len(word2)<len(word)-1:
    continue
  
  if len(word2)==len(word)+1:
    cnt1+=1
    cnt2+=1

  if len(word2)+1==len(word):
    cnt1+=1
    cnt2+=1

  listword2=list(word2)
  for i in word:
    if i not in listword2:
      cnt1+=1
      
    if i in listword2:
      listword2[listword2.index(i)]="없음"
      
  listword=list(word)
  for i in word2:
    if i not in listword:
      cnt2+=1
    if i in listword:
      listword[listword.index(i)]="없음"

  if cnt1<cnt2:
    cnt1=cnt2

  if cnt1<2:
    total+=1

print(total)