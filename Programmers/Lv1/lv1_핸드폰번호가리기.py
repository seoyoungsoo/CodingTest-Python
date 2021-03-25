# 핸드폰 번호 가리기

# 나의 풀이
# 효율성 측면에서 문제가 많은듯
def solution(phone_number):
    pNum = list(phone_number)

    for idx in range(len(phone_number)-5, -1, -1):
        del pNum[idx]
        pNum.insert(idx, '*')

    return ''.join(pNum)


# 다른 풀이
def otherSol(s):
    return '*' * (len(s) - 4) + s[-4:]


# testcase1
phone_number = "01033334444"
print(solution(phone_number))
print(otherSol(phone_number))