# 실패율

# 나의 풀이
def solution(N, stages):
    clear = len(stages)
    per = {}  # dictionary 사용

    for i in range(1, N + 1):
        if stages.count(i) == 0:  # 0/0의 경우에 해당
            per[i] = 0
        else:
            cnt = stages.count(i)
            fail = (cnt / clear)
            clear -= cnt
            per[i] = fail

    res = sorted(per, key=lambda x: per[x], reverse=True)
    '''per는 dictionary이므로 sorted에 per을 그냥 넘기면 per의 keys가 들어간다.
    그러므로 keys는 생략이 가능하고, lambda는 기준을 per[x] 즉, value로 정렬한다.
    결과적으로 key가 출력됨'''
    # lambda를 좀 더 다뤄보자

    return res


# testcase1
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
