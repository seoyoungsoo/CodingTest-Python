# 10974번 모든 순열
from itertools import permutations
import sys
input = sys.stdin.readline

N = [i for i in range(1, int(input())+1)]
lst = list(permutations(N, len(N)))

for l in lst:
    print(' '.join(map(str, l)))