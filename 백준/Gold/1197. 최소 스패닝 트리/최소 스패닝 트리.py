from sys import stdin


input = stdin.readline
num_v, num_e = map(int, input().split())
edges = []  # tuple : (v1, v2, cost)
for _ in range(num_e):
    edges.append(tuple(map(int, input().split())))
edges.sort(key=lambda x: x[2])  # cost 기준 정렬
parent = [i for i in range(num_v + 1)]

# 루트 반환
def find_parent(v):
    if parent[v] == v:
        return v
    parent[v] = find_parent(parent[v])  # 압축
    return parent[v]


# 다른 그룹 합치기
def union(root1, root2):
    if root1 < root2:
        parent[root2] = root1
    else:
        parent[root1] = root2


# 같은 그룹이면 return False, 다른 그룹이면 같은 그릅으로 만들고 return True
def is_same_group(v1, v2) -> bool:
    root1, root2 = find_parent(v1), find_parent(v2)
    if root1 == root2:
        return True
    union(root1, root2)
    return False


cnt = 0
result = 0
for edge in edges:
    v1, v2, cost = edge
    if is_same_group(v1, v2):
        continue
    result += cost
    cnt += 1
    if cnt == num_v - 1:
        break

print(result)