# 13335번 트럭
# 코드참조: https://deok2kim.tistory.com/137
from collections import deque

n, w, l = map(int, input().split())
trucks = deque(map(int, input().split()))
road = deque()
t_time = deque()
time = 0

while t_time or trucks:
    time += 1
    if road:
        if t_time[0] + w == time:
            road.popleft()
            t_time.popleft()

    if trucks:
        if sum(road) + trucks[0] <= l:
            road.append(trucks.popleft())
            t_time.append(time)

print(time)