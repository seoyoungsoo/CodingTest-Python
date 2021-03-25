# 10816번 숫자카드2
# 코드 참조 // https://infinitt.tistory.com/288

n = int(input())
card = (list(map(int, input().split())))
m = int(input())
compare = list(map(int, input().split()))

dic = dict()

for i in card:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for j in compare:
    if j in dic:
        print(dic[j], end=" ")
    else:
        print(0, end=" ")