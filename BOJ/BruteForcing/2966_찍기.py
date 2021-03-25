# 2966번 찍기

n = int(input())
m = input()

adrian = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']
score = {'Adrian':0, 'Bruno':0, 'Goran':0}

for idx, answer in enumerate(m):
    if answer == adrian[idx % len(adrian)]:
        score['Adrian'] += 1
    if answer == bruno[idx % len(bruno)]:
        score['Bruno'] += 1
    if answer == goran[idx % len(goran)]:
        score['Goran'] += 1

count = max(score.values())

print(count)
for name, value in score.items():
    if value == count:
        print(name)