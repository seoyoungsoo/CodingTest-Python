# 다음 큰 숫자

# 나의 풀이
def solution(n):
    nbin = format(n, 'b').count('1')

    while True:
        n += 1
        if format(n, 'b').count('1') == nbin:
            return n


# testcase1
n = 78
print(solution(n))