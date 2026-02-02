N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)
Y = 0
ans = 0
for i in range(N):
    ans += 1
    if i < (N - K):
        continue
    Y += A[i]
    if Y >= X:
        break
if Y < X:
    print(-1)
else:
    print(ans)
