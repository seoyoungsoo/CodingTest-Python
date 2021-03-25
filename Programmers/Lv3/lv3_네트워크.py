# 네트워크

def network(computers, checked, num):
    stack = [num]

    while stack:
        n = stack.pop()
        if n not in checked:
            checked.append(n)
            for i in range(len(computers[num])):
                if computers[n][i] == 1 and i not in checked:
                    stack.append(i)


def solution(n, computers):
    answer = 0
    checked = []

    for i in range(len(computers)):
        if i not in checked:
            network(computers, checked, i)
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
