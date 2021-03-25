# 2309번 일곱 난쟁이
# 3040번 백설 공주와 일곱 난쟁이

dwarf = list()
for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()
tall = sum(dwarf) - 100
for k in range(len(dwarf)-1):
    for j in range(k + 1, len(dwarf)):
        if dwarf[k] + dwarf[j] == tall:
            dwarf.pop(j)
            dwarf.pop(k)
            break

for i in range(len(dwarf)):
    print(dwarf[i])
