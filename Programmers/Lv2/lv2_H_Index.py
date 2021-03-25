# H-Index

# 나의 풀이
def solution(citations):
    answer = 0

    if min(citations) > len(citations):
        return len(citations)
    if max(citations) == 0:
        return answer

    for i in range(1, len(citations) + 1):
        cnt = 0
        for j in citations:
            if i <= j:
                cnt += 1
        if i <= cnt and cnt > answer:
            answer = i
    return answer


# 다른 풀이1
def otherSol1(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l - i:
            return l - i
    return 0


# 다른 풀이2
# sort로 정렬해서 가장 큰 값부터 작은 값으로 정렬한 후,
# enumerate로 (idx, value)형태로 묶음
# 그 후 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고
# 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나옴
# 이를 map으로 묶으면, 한 value 입장에서 보는 최솟값 value의 집합이 나옴
# 즉 h 값들의 집합이 나오는데, 이 중 최대값을 max로 뽑아서 출력하는 방식
def otherSol2(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


# testcase1
citations = [3, 0, 6, 1, 5]
print(solution(citations))
print(otherSol1(citations))