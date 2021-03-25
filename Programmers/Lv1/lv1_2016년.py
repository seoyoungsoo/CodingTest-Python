# 2016년

def solution(a, b):
    day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = 0

    for i in month[:a-1]:
        date += i

    date += b

    return day[date % 7]


# testcase 1
a = 5
b = 24
print(solution(a, b))