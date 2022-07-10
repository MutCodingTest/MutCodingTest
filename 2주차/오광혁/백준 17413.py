# 단어 뒤집기2/문자열

s = input()
tag = False
word = ''
stack = ''

for i in s:
    if tag == False:
        # 뒤집어서 출력
        if i == '<':
            tag = True
            word += i
        
        elif i == ' ':
            word += i
            stack += word
            word = ""
        
        else:
            word = i + word
    
    else:
        word += i

        if i == '>':
            tag = False
            stack += word
            word = ""

print(stack + word)