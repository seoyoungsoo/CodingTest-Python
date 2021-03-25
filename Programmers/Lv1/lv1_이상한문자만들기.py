# 이상한 문자 만들기

def solution(s):
    answer = ''

    count = 0
    for i in s:
        if i == ' ':
            count = 0
            answer += ' '
        else:
            if count % 2 == 0:
                answer += i.upper()
                count += 1
            else:
                answer += i.lower()
                count += 1

    return answer


# testcase1
s = "try hello world"
print(solution(s))