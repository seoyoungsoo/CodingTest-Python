# 1439번 뒤집기

s = input()
dic = dict()
dic['0'], dic['1'] = 0, 0

tmp = s[0]

for i in s:
    if tmp != i:
        dic[tmp] += 1
        tmp = i
dic[tmp] += 1
print(min(dic.values()))