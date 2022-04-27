from collections import defaultdict, deque


def dfs(table, point, route):
    while table[point]:
        dfs(table, table[point].popleft(), route)
    route.append(point)


def solution(tickets):
    table = defaultdict(deque)
    tickets.sort()
    for u, v in tickets:
        table[u].append(v)
    route = []
    dfs(table, "ICN", route)
    route.reverse()
    return route

"""
def dfs(table, visited, start, upper, path, res):
    if res:
        return
    if len(path) == upper:
        for item in path:
            res.append(item)
        return
    for i, end in enumerate(table[start]):
        if (start, i) not in visited:
            visited.add((start, i))
            dfs(table, visited, end, upper, path + [end], res)
            visited.remove((start, i))

def solution(tickets):
    table = defaultdict(list)
    for u, v in tickets:
        table[u].append(v)
    for k in table:
        table[k].sort()
    res = []
    dfs(table, set(), "ICN", len(tickets) + 1, ["ICN"], res)  # (table, start_point, upper ,path)
    return res
"""