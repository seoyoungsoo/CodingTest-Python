# 가운데 글자 가져오기

def solution(s):
    answer = ''

    slen = len(s)
    if slen % 2 == 0:
        mid = int(slen / 2 - 1)
        answer += s[mid]
        answer += s[mid + 1]
    else:
        mid = int(slen / 2)
        answer += s[mid]

    return answer


# testcase 1
s = "abcde"
print(solution(s))
