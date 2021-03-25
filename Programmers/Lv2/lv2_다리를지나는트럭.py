# 다리를 지나는 트럭

# 나의 풀이
# deque를 써서 풀 수도 있겠다
def solution(bridge_length, weight, truck_weight):
    res = 0  # 걸리는 시간
    bridge_on = [0] * bridge_length
    crnt_weight = 0  # 다리 위 트럭의 무게

    while truck_weight:  # 트럭이 존재하는 동안 반복
        res += 1
        bridge_out = bridge_on.pop(0)
        crnt_weight -= bridge_out

        if crnt_weight + truck_weight[0] <= weight:
            truck = truck_weight.pop(0)
            bridge_on.append(truck)
            crnt_weight += truck
        else:
            bridge_on.append(0)

    while crnt_weight > 0:  # 다리 위에 존재하는 트럭이 지나갈 때 까지 반복
        res += 1
        bridge_out = bridge_on.pop(0)
        crnt_weight -= bridge_out

    return res


# testcase1
bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
print(solution(bridge_length, weight, truck_weights))