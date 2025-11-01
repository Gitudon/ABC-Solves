N, M = map(int, input().split())
S = [0] * N
for i in range(N):
    S[i] = input()

ans = set()
for i in range(N - M + 1):
    for j in range(N - M + 1):
        buf = ""
        for k in range(i, i + M):
            buf += S[k][j : j + M]
        ans.add(buf)

print(len(ans))
