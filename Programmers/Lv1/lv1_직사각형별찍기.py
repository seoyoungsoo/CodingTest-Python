# 직사각형 별찍기

# 나의 풀이
a, b = map(int, input().strip().split(' '))

for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

'''
# 다른 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*' * a + '\n') * b
print(answer)
'''