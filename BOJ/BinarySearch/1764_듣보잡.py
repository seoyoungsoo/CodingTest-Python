# 1764번 듣보잡

n, m = map(int, input().split())

notListen, notSee = list(), list()
for i in range(n+m):
    if i < n:
        notListen.append(input())
    else:
        notSee.append(input())

# 나의 풀이
# 시간초과가 발생함
'''ls = list()
notListen.sort()
notSee.sort()
for i in notListen:
    for j in notSee:
        if i == j:
            ls.append(i)
            break
'''

# 해결법
# set 의 교집합 성질을 이용해서 문제를 풀이
ls = sorted(list(set(notListen) & set(notSee)))
print(len(ls))
for i in ls:
    print(i)
