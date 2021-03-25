# 소수 찾기
# 에라토스테네스의 체를 이용(효율성 고려)

def solution(n):
    prime = [True] * (n + 1)  # 모든 수를 나열하기 위해서
    length = int(n ** 0.5)  # 최대 배수를 선정하는 기준을 만들어 반복 낭비를 제거

    for i in range(2, length + 1):
        if prime[i]:
            for j in range(i + i, n + 1, i):  # 자기 자신은 남겨야하기 때문에 i+i 부터 소수 아닌 수를 제거
                prime[j] = False

    return len([i for i in range(2, n + 1) if prime[i]])


# 다른 풀이
def prime_list(n):
    num = set(range(2, n+1))  # 2 ~ n 까지의 수를 num에 입력

    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))  # i가 num 안에 있으면, i의 배수 set을 num에서 빼줌

    return len(num)  # 나머지 num의 길이 리턴


# testcase1
n = 10
print(solution(n))