# 시저 암호

# 문자를 ASCII 코드로 변환하는 함수 ord() 함수
# ASCII 코드를 문자로 변환하는 함수 chr() 함수
# ASCII A = 65, Z = 90, a = 97, z = 122, 알파벳의 개수 26

def solution(s, n):
    answer = ''

    for i in s:
        if i == ' ':
            answer += ' '
        else:
            if i.islower():
                answer += chr(97 + (ord(i) + n - 97) % 26)
            else:
                answer += chr(65 + (ord(i) + n - 65) % 26)

    return answer


# testcase1
s = "AB"
n = 1
print(solution(s, n))