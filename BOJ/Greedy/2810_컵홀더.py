# 2810번 컵홀더

n = int(input())
seat = input()

tmp = seat.count('LL')
print(min(n, n+1-tmp))