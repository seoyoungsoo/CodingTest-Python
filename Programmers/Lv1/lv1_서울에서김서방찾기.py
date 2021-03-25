# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    idx = seoul.index('Kim')
    answer += f"김서방은 {idx}에 있다"

    return answer


# 다른 풀이
def sol(seoul):
    return ("김서방은 " + str(seoul.index('Kim')) + "에 있다")


# testcase 1
seoul = ["Jane", "Kim"]
print(solution(seoul))