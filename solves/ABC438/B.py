N, M = map(int, input().split())
S = input()
T = input()

ans = 10**10
for i in range(N - M + 1):
    sub = S[i : i + M]
    buf = 0
    for j in range(M):
        if int(S[i + j]) < int(T[j]):
            buf += (10 + int(S[i + j])) - int(T[j])
        else:
            buf += int(S[i + j]) - int(T[j])
    ans = min(ans, buf)

print(ans)
