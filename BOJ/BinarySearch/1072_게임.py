# 1072번 게임
# 코드 참조 // https://suri78.tistory.com/214

x, y = map(int, input().split())

now_z = int(y * 100 / x)
s, e = 1, 1000000000
if now_z >= 99:
    print(-1)
else:
    while s < e:
        m = (s + e) // 2
        mv = int((y + m) * 100 / (x + m))
        if mv <= now_z:
            s = m + 1
        else:
            e = m
    print(e)
