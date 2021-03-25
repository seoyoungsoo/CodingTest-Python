# 10815번 숫자 카드

# set을 사용해 풀 수도 있지만 주제에 맞게 이분 탐색으로 풀어보려고 노력함
# 시간초과가 떠서 다른 코드를 찾아봤는데 이유를 모르겠다.
# 참조 https://yoonsang-it.tistory.com/50 // + dict를 사용한 풀이법
def cmpCard(card, num):
    if len(card) == 1:
        if card[0] == num:
            return 1
        else:
            return 0

    medium = len(card) // 2
    if card[medium] == num:
        return 1
    elif card[medium] < num:
        return cmpCard(card[medium:], num)
    else:
        return cmpCard(card[:medium], num)


n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
compare = list(map(int, input().split()))

answer = list()
for num in compare:
    j = cmpCard(card, num)
    print(j, end=' ')
