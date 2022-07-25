n,k=map(int,input().split())

initwords=list(input())

def change(words):
  copywords=words.copy()
  for i in range(len(words)):
    now=i
    back=i-1
    front=i+1
    if front==len(words):
      front=0
    wordlist=[copywords[back],copywords[now],copywords[front]]
    setwordlist=set(wordlist)
    if (len(setwordlist)==1) or (len(setwordlist)==len(wordlist)):
      words[now]="B"    
    elif (wordlist.count("R")==2 and wordlist.count("G")==1) or (wordlist.count("G")==2 and wordlist.count("B")==1) or (wordlist.count("B")==2 and wordlist.count("R")==1):
      words[now]="R"
    else:
      words[now]="G"
for _ in range(k):
  change(initwords)

print(initwords.count("R"),end=" ")
print(initwords.count("G"),end=" ")
print(initwords.count("B"))
