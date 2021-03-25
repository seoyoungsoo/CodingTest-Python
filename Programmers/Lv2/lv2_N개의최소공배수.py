# N개의 최소공배수

# 나의 풀이
def gcd(x, y):  # 최대공약수를 구하는 함수
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):  # 최소공배수를 구하는 함수
    return x * y // gcd(x, y)


def solution(arr):
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]


# 다른 풀이
def otherSol(arr):
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        a = arr[i]
        b = arr[i+1]
        while a % b:
            r = a % b
            a, b = b, r
        arr[i+1] = (arr[i] + arr[i+1]) / b
    return arr[-1]

# testcase1
arr = [2, 6, 8, 14]
print(solution(arr))
print(otherSol(arr))