# 1543번 문서 검색
# 코드 참조: https://kils-log-of-develop.tistory.com/195

word = input()
f = input()
cnt, i = 0, 0

while len(word) - i >= len(f):
    if word[i:i+len(f)] == f:
        cnt += 1
        i += len(f)
    else:
        i += 1
print(cnt)

# 나의 풀이
# 왜 틀리는지 알아봐야겠다.
'''
word = input()
f = input()
cnt, i = 0, 0

while True:
    if f in word[:(len(f) + i)]:
        word = word[(len(f)+i):]
        i = 0
        cnt += 1

    if f not in word:
        break

    if len(f) + i < len(word):
        i += 1
print(cnt)

'''