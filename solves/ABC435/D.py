# WA解です

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
s = [0] * (N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

memo = [-1] * (N + 1)


def dfs(v):
    if s[v]:
        return True
    if memo[v] != -1:
        return memo[v] == 1

    visited[v] = True
    result = False
    for v_next in graph[v]:
        if not visited[v_next]:
            if dfs(v_next):
                result = True
                break

    visited[v] = False
    memo[v] = 1 if result else 0
    return result


Q = int(input())
for _ in range(Q):
    typ, v = map(int, input().split())
    if typ == 1:
        s[v] = 1
    elif typ == 2:
        visited = [False] * (N + 1)
        if dfs(v):
            print("Yes")
        else:
            print("No")
