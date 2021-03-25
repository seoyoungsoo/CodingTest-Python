# 2858번 기숙사 바닥

R, B = map(int, input().split())

for i in range(1, int(B ** 0.5) + 1):
    if B % i == 0:
        j = B // i
        if (i + j) * 2 + 4 == R:
            print(j+2, i+2)