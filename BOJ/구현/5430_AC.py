# 5430번 AC
from collections import deque

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')
    q = deque()

    for num in arr:
        if num.isdigit():
            q.append(num)

    reverse = False

    for i in p:
        if i == 'R':
            reverse = not reverse
        else:
            try:
                if reverse:
                    q.pop()
                else:
                    q.popleft()
            except IndexError:
                print('error')
                break
    else:
        if reverse:
            q.reverse()

        print('[' + ','.join(q) + ']')