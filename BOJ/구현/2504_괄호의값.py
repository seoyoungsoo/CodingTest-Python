# 2504번 괄호의 값
import sys
input = sys.stdin.readline

# 처음 입력 받을 때 strip()을 사용하지 않자 런타임 에러가 발생했다.
# 오래된 데이터의 경우 데이터의 끝에 '\n'이 없는 경우가 존재한다.
# 내용참조: https://www.acmicpc.net/board/view/26004
string = list(map(str, input().strip()))
stack = []
cnt = 0

for s in string:
    if s == ')':
        tmp = 0
        while stack:
            n = stack.pop()
            if n == '(':
                if tmp:
                    stack.append(2 * tmp)
                else:
                    stack.append(2)
                break
            elif n == '[':
                print(0)
                exit(0)
            else:
                tmp += n
    elif s == ']':
        tmp = 0
        while stack:
            n = stack.pop()
            if n == '[':
                if tmp:
                    stack.append(3 * tmp)
                else:
                    stack.append(3)
                break
            elif n == '(':
                print(0)
                exit(0)
            else:
                tmp += n
    else:
        stack.append(s)

if '(' in stack or '[' in stack:
    print(0)
    exit(0)
else:
    print(sum(stack))