N, M = map(int, input().split())
graph = [1] * N
for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1] += 1
    graph[B - 1] += 1


def n_c_3(member):
    n = N - member
    if n <= 2:
        return 0
    return n * (n - 1) * (n - 2) // 6


ans = []
for i in range(N):
    ans.append(n_c_3(graph[i]))
print(*ans)
