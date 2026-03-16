N, M = map(int, input().split())
C = list(map(int, input().split()))
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())

ans = 0
for i in range(N):
    if C[A[i] - 1] != 0:
        if B[i] < C[A[i] - 1]:
            ans += B[i]
            C[A[i] - 1] -= B[i]
        else:
            ans += C[A[i] - 1]
            C[A[i] - 1] = 0
print(ans)
