# 17413번 단어 뒤집기 2

s = list(input())
tag = False
result = ''
tmp = ''

for i in s:
    if not tag:
        if i == '<':
            tag = True
            tmp += i
        elif i == ' ':
            tmp += i
            result += tmp
            tmp = ''
        else:
            tmp = i + tmp

    elif tag:
        tmp += i
        if i == '>':
            tag = False
            result += tmp
            tmp = ''

print(result + tmp)