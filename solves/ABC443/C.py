N, T = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
start = 0
for i in range(N):
    if A[i] >= start:
        ans += A[i] - start
        start = A[i] + 100

if T >= start:
    ans += T - start
print(ans)
