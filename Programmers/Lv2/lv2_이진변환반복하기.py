# 이진 변환 반복하기

# 나의 풀이
def solution(s):
    bincount = 0
    zero = 0
    while len(s) > 1:
        tmp = ''
        for i in s:
            if not int(i):
                zero += 1
            else:
                tmp += i
        s = format(len(tmp), 'b')
        bincount += 1
    return [bincount, zero]


# testcase1
s = '110010101001'
print(solution(s))