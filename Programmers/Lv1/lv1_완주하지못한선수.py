# 완주하지 못한 선수

def solution(participant, completion):
    answer = ''
    hash_1 = {}

    for name in completion:
        if name in hash_1:
            hash_1[name] += 1
        else:
            hash_1[name] = 1

    for key in participant:
        if key in hash_1:
            hash_1[key] -= 1
            if hash_1[key] < 0:
                answer = key
        else:
            answer = key
    return answer


# testcase 1
part = ['leo', 'kiki', 'eden']
complete = ['eden', 'kiki']

print(solution(part, complete))
