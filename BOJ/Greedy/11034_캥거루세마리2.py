# 11034번 캥거루 세마리 2

while True:
    try:
        A, B, C = list(map(int, input().split()))
        count = 0

        if C - B > B - A:
            print(C - B - 1)
        else:
            print(B - A - 1)
    except:
        break
