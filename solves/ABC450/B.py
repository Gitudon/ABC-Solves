N = int(input())

graph = [[0] * N for _ in range(N - 1)]
for i in range(N - 1):
    C = list(map(int, input().split()))
    for j in range(i + 1, N):
        graph[i][j] = C[j - i - 1]


ans = "No"
for a in range(N - 2):
    for b in range(a + 1, N - 1):
        for c in range(b + 1, N):
            if graph[a][c] > graph[a][b] + graph[b][c]:
                ans = "Yes"
print(ans)
