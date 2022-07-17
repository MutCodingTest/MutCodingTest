t=int(input())

def square(x,y):
  global head
  for word in words:
    if word=="R":
      if head=="UP":
        head="RIGHT"
      elif head=="DOWN":
        head="LEFT"
      elif head=="RIGHT":
        head="DOWN"
      elif head=="LEFT":
        head="UP"
    elif word=="L":
      if head=="UP":
        head="LEFT"
      elif head=="DOWN":
        head="RIGHT"
      elif head=="RIGHT":
        head="UP"
      elif head=="LEFT":
        head="DOWN"
    elif word=="F":
      if head=="UP":
        y+=1
        ylist.append(y)
      elif head=="DOWN":
        y-=1
        ylist.append(y)
      elif head=="RIGHT":
        x+=1
        xlist.append(x)
      elif head=="LEFT":
        x-=1
        xlist.append(x)
    elif word=="B":
      if head=="UP":
        y-=1
        ylist.append(y)
      elif head=="DOWN":
        y+=1
        ylist.append(y)
      elif head=="RIGHT":
        x-=1
        xlist.append(x)
      elif head=="LEFT":
        x+=1
        xlist.append(x)

for _ in range(t):
  words=input()
  head="UP"
  xlist=[0]
  ylist=[0]

  square(0,0)
  lenx=max(xlist)-min(xlist)
  leny=max(ylist)-min(ylist)
  
  print(lenx*leny)
        
      
        
      
    