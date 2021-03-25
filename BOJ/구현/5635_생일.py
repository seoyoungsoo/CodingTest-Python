# 5635번 생일
import sys
input = sys.stdin.readline

n = int(input())
student = [0 for _ in range(n)]

for i in range(n):
    name, d, m, y = map(str, input().split())

    student[i] = [name, int(d), int(m), int(y)]

student.sort(key=lambda x: (x[3], x[2], x[1]))

print(student[-1][0])
print(student[0][0])