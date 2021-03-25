# [1차] 비밀지도

# 나의 풀이
def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        '''barr1.append(format(arr1[i], 'b').zfill(n))
        barr2.append(format(arr2[i], 'b').zfill(n))'''
        tmp = ''

        barr1 = format(arr1[i], 'b').zfill(n)
        barr2 = format(arr2[i], 'b').zfill(n)

        for j in range(n):
            if int(barr1[j]) == 0 and int(barr2[j]) == 0:
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)

    return answer


# 다른 풀이
# zip, bin, rjust, replace 를 이용한 풀이
# 위의 내장함수의 사용법을 이해하자
def otherSol(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a12 = str(bin(i | j)[2:])
        a12 = a12.rjust(n, '0')
        a12 = a12.replace('1', '#')
        a12 = a12.replace('0', ' ')
        answer.append(a12)

    return answer


# testcase1
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
print(otherSol(n, arr1, arr2))
