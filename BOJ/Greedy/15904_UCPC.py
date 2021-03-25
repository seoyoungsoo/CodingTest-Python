# 15904번 UCPC

text = input()
answer = ['U', 'C', 'P', 'C']
flag = True

for i in range(len(answer)):
    if answer[i] in text:
        text = text[text.find(answer[i]) + 1:]
    else:
        flag = False
        break

if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")