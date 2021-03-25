# 조이스틱

"""
"AABAAAAAAABBB"의 경우 11이 최소 조작 횟수가 되어야 하는데
구글링 해서 찾아본 다른 코드의 경우도 통과하지 못함
제출 결과는 전부 통과로 문제에 오류가 있다.
"""


# 나의 풀이
def solution(name):
    # 상하 조정으로 알파벳 변경
    arr = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name]
    idx, answer = 0, 0

    while True:
        answer += arr[idx]
        arr[idx] = 0
        if sum(arr) == 0:
            return answer

        # 좌우 이동방향 정하기
        left, right = 1, 1
        while arr[idx - left] == 0:
            left += 1
        while arr[idx + right] == 0:
            right += 1

        # 위치(인덱스) 조정
        answer += left if left < right else right
        idx += -left if left < right else right


# testcase1
name = "JEROEN"
print(solution(name))