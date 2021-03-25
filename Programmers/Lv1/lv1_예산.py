# 예산

# 나의 풀이
# 필요없는 코드가 많은 듯
def solution(d, budget):
    cnt, tmp = [], 0
    d.sort()

    for idx in range(0, len(d)):
        if budget >= d[idx]:
            budget -= d[idx]
            tmp += 1
            if idx == len(d) - 1:
                cnt.append(tmp)
        else:
            cnt.append(tmp)
            tmp = 0

    return max(cnt)


# 다른 풀이1
# 나와 같은 방식으로 풀었지만 불필요한 코드를 제거해 좀 더 간결하게 해결
def otherSol1(d, budget):
    cnt = 0
    d.sort()
    for idx in range(len(d)):
        if d[idx] <= budget:
            cnt += 1
            budget -= d[idx]
        else:
            break
    return cnt


# 다른 풀이2
# sum()이 반복되어 시간 복잡도가 O(n^2)되어 사실상 위의 풀이가 낫지만
# 이런 방식으로도 접근할 수 있다는 것을 알기 위해 작성해봄
def otherSol2(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# testcase1
d = [1, 3, 2, 5, 4]
budget = 9
print(solution(d, budget))
print(otherSol1(d, budget))
print(otherSol2(d, budget))
