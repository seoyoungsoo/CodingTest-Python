# 주식가격

# 나의 풀이
# 시간복잡도가 O(n^2)이 된다.
def solution(prices):
    answer = []

    for i in range(0, len(prices) - 1):
        cnt = 0
        for j in range(i + 1, len(prices)):
            if prices[j] >= prices[i]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)

    answer.append(0)

    return answer


# 다른 풀이1
# 나와 같은 풀이지만 파이썬의 특징을 잘 살린 것 같다.
def otherSol1(prices):
    answer = [0] * len(prices)
    # answer = [0 for a in range(len(prices))] 도 된다.

    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


# 다른 풀이2
# 스택을 이용한 풀이로 최선의 경우 O(n)으로 충분하다.
# 핵심은 반복문을 계속 진행하면서 현재 시점보다 가격이 높은 시점이 언제였는지 되짚어가면서 판단하는 방식
def otherSol2(prices):
    # 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices) - i - 1 for i in range(len(prices))]

    # prices의 인덱스를 차례로 담아두는 배열
    stack = [0]

    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]

            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()

            # 떨어지지 않았다면 다음 시점으로 넘어감
            else:
                break
        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정
        stack.append(i)

    return answer


# testcase1
prices = [1, 2, 3, 2, 3]
print(solution(prices))
print(otherSol2(prices))