# 기능개발

# 나의 풀이
# zip 을 이용해서 해결하고 싶었다..
def solution(progresses, speeds):
    answer = []

    while True:
        cnt = 0
        if len(progresses) < 1:
            break
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        for i in range(len(progresses)):
            if progresses[i] < 100:
                break
            else:
                cnt += 1

        for j in range(cnt):
            progresses.pop(0)
            speeds.pop(0)
        if cnt:
            answer.append(cnt)

    return answer


# 다른 풀이1
def otherSol(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


# 다른 풀이 2
def otherSol2(progresses, speeds):
    answer = []

    while progresses:
        progresses = [x + y for x, y in zip(progresses, speeds)]
        pop_count = 0

        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            pop_count += 1

        if pop_count is not 0:
            answer.append(pop_count)

    return answer


# testcase1
progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses, speeds))
print(otherSol(progresses, speeds))
