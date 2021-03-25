prefer = dict()
contents = ['A','B','C','D','E']
num = list(map(float, input().split()))

for i in range(len(num)):
    prefer[contents[i]] = num[i]

n, m = map(int, input().split())

browse = [input() for _ in range(n)]
genre = [input() for _ in range(n)]

res = []

for i in range(n):
    for j in range(m):
        if browse[i][j] != 'W':
            if browse[i][j] == 'Y':
                res.append([0, genre[i][j], prefer[genre[i][j]], i, j])
            else:
                res.append([1, genre[i][j], prefer[genre[i][j]], i, j])
res.sort(key=lambda x: (x[0], -x[2], x[3], x[4]))
for r in res:
    print(*r[1:])