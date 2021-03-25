# 2798번 블랙잭

# 나의 풀이
# itertools를 활용해 3개의 카드를 뽑는 경우의 수를 모두 정리 후 m 값보다 낮거나 같으면 후보에 넣는 식으로 진행
from itertools import combinations

n, m = map(int, input().split())

card = list(map(int, input().split()))
card = list(combinations(card, 3))

jack = list()
'''
itertools를 사용하지 않고 combinations를 구현해보자
for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            jack.append(sum([card[i],card[j],card[k]]))
            
jack = [i for i in jack if i <= m]
print(max(jack))
'''
for i in card:
    if sum(i) <= m:
        jack.append(sum(i))
print(max(jack))

