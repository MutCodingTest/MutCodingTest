n=int(input())
for _ in range(n):
  a,b=input().split()
  
  anagram=True
  
  for i in a:
    if i not in b:
      anagram=False

  for i in b:
    if i not in a:
      anagram=False
  
  if anagram==True:
    print(a,"&",b,"are anagrams.")
  else:
    print(a,"&",b,"are NOT anagrams.")
