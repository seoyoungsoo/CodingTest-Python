# 최댓값과 최솟값

# 나의 풀이
def solution(s):
    arr = list()
    tmp = ''
    for i in range(len(s)):
        if s[i] == ' ':
            arr.append(int(tmp))
            tmp = ''
        else:
            tmp += s[i]
    arr.append(int(tmp))

    return str(min(arr)) + ' ' + str(max(arr))


# 다른 풀이
# 같은 접근방식이지만 좀 더 파이썬다운 코드
def otherSol(s):
    s = list(map(int, s.split()))
    return str(min(s)) + " " + str(max(s))


# testcase1
s = '-1 -2 -3 -4'
print(solution(s))
print(otherSol(s))
