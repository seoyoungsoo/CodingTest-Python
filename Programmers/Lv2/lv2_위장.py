# 위장

# 나의 풀이
# 문제 취지에 맞는 해시 풀이
def solution(clothes):
    cnt = 1
    dic = dict()

    for _, kind in clothes:
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1
    for val in dic.values():
        cnt *= (val + 1)

    return cnt - 1


# 다른 풀이
# Counter와 reduce를 이용한 풀이
def otherSol(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for _, kind in clothes])
    answer = reduce(lambda x, y: x * (y+1), cnt.values(), 1) - 1
    return answer


# testcase1
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"],
           ["green_turban", "headgear"]]
print(solution(clothes))
print(otherSol(clothes))