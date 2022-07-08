from sys import stdin

input = stdin.readline

n, m = map(int, input().split())
known = input().rstrip()
parties = [list(map(int, input().split()[1:])) for _ in range(m)]
parent = [i for i in range(n + 1)]

answer = 0


def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x


def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root > b_root:
        a, b = b, a
        a_root, b_root = b_root, a_root
    origin_root = parent[b]
    parent[b] = a_root
    for i in range(1, len(parent)):
        if parent[i] == origin_root:
            parent[i] = a_root


if known == "0":
    print(len(parties))
else:
    # 1. 그룹화
    for party in parties:
        for i in range(len(party) - 1):
            union(party[i], party[i + 1])
    # 2. 거짓말쟁이인지 알고 있는 사람들 모두 찾기
    known = set(map(int, known.split()[1:]))
    for bad in list(known):
        bad_root = find(bad)
        for i in range(1, len(parent)):
            if parent[i] == bad_root:
                known.add(i)
    # 3. 각 파티를 돌면서 알고있는 사람이 한명도 없으면 answer += 1
    for party in parties:
        if len(known & set(party)) == 0:
            answer += 1
    print(answer)
