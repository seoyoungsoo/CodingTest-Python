# 10988번 팰린드롬인지 확인하기

word = input()

n = len(word) % 2
half = len(word)//2

w1 = w2 = ''

if not n:
    w1 = list(word[:half])
    w2 = list(reversed(word[half:]))
else:
    w1 = list(word[:half])
    w2 = list(reversed(word[half+1:]))

for i in range(len(w1)):
    if w1[i] != w2[i]:
        print(0)
        exit(0)
print(1)