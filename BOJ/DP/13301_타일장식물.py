# 13301번 타일 장식물

n = int(input())

a, b = 1, 1

for i in range(n):
    a, b = b, a + b

print(b*2)