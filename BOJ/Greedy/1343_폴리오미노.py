# 1343번 폴리오미노
import sys

board = input()

bList = board.split('.')

for i, v in enumerate(bList):
    if v != '':
        if len(v) % 2:
            print(-1)
            sys.exit()
        else:
            tmp = ''
            tmp += 'AAAA' * (len(v) // 4)
            tmp += 'B' * (len(v) % 4)
            bList[i] = tmp
print('.'.join(bList))

# replace 함수를 사용한 구현방법
'''
board = input()
board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)
'''