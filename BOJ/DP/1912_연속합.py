# 1912번 연속합
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 내가 작성한 코드는 시간 초과가 났다.
# 최대 값을 계속해서 갱신해주는 방식이라 그런 것 같다.
# 코드 참조: https://wook-2124.tistory.com/406
'''sumArr = min(arr)

for i in range(n):
    tmp = arr[i]
    for j in range(i+1, n):
        if tmp > sumArr:
            sumArr = tmp
        tmp += arr[j]
print(sumArr)'''

for i in range(1, n):
    arr[i] = max(arr[i], arr[i-1]+arr[i])

print(max(arr))
