# 전화번호 목록

# 나의 풀이
# 입력이 많아지면 효율성에서 걸리지 않을까..
def solution(phone_book):
    answer = False
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i] in phone_book[j]:
                return answer
            else:
                answer = True
    return answer


# 다른 풀이
# 문제의 취지에 맞게 해시를 이용한 정석적인 풀이
def otherSol(phone_book):
    answer = True
    hash = {}
    for num in phone_book:
        hash[num] = 1
    for num in phone_book:
        tmp = ''
        for n in num:
            tmp += n
            if tmp in hash and tmp != num:
                answer = False
    return answer


# testcase1
phone_book = ['119', '97674223', '1195524421']
print(solution(phone_book))
print(otherSol(phone_book))
