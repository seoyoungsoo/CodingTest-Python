# 구명보트

# 나의 풀이
# pop(0)의 경우, 데이터를 지우고 한 칸씩 앞으로 당기기 때문에 O(n)이 소모되어 효율성 측면에서 안좋음
# 이를 해결하기 위해 deque를 통한 popleft() 를 이용
def solution(people, limit):
    from collections import deque as dq

    answer = 0
    q = dq(sorted(people))

    while q:
        if len(q) < 2:
            q.pop()
            answer += 1
        else:
            if q[-1] + q[0] <= limit:
                answer += 1
                q.popleft()
                q.pop()
            else:
                answer += 1
                q.pop()

    return answer


# 다른 풀이
# 풀이 방식이 너무 참신하다. 이런 생각을 할 수 있다는게 대단
def otherSol(people, limit):
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b:
        if people[b] + people[a] <= limit:
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer


# testcase1
people = [80, 70, 60, 55, 45, 40]
limit = 100
print(solution(people, limit))
print(otherSol(people, limit))