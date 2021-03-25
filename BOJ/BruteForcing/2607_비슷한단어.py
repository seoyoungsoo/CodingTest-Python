# 2607번 비슷한 단어
import sys

input = sys.stdin.readline

N = int(input())
word = input()
cnt = 0

for i in range(N - 1):
    tmp = list(word)
    cmpWord = list(input())

    if len(cmpWord) >= len(word):
        while tmp:
            s = tmp.pop()
            if s in cmpWord:
                cmpWord.remove(s)

        if len(cmpWord) <= 1:
            cnt += 1
    else:
        while cmpWord:
            s = cmpWord.pop()
            if s in tmp:
                tmp.remove(s)

        if len(tmp) <= 1:
            cnt += 1
print(cnt)