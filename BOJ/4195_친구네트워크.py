# 4195번 친구 네트워크
"""
Union-Find 알고리즘을 이해하고 풀어야 하는 문제이다.
Union-Find 알고리즘이란?
1. 처음의 각각의 원소는 연결된 정보가 없기 때문에 부모로 자기 자신을 가지고 있다.
2. find(x) 함수: x로 들어온 원소의 Root 노드를 반환한다.
3. union(x, y) 함수: y의 Root 노드를 x로 만드는 함수
"""


# Root node를 찾아주는 함수
def find(x):
    if x == parent[x]:
        return x
    else:
        root_x = find(parent[x])
        parent[x] = root_x
        return parent[x]


# y의 Root 노드가 x의 Root 노드와 같지 않으면
# y의 Root 노드가 x의 Root 노드의 자식이 되도록 하는 함수
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]


N = int(input())

for _ in range(N):
    parent = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x, y)
        print(number[find(x)])
