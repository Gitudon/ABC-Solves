N, X, Y = map(int, input().split())
A = list(map(int, input().split()))


def floor(a, b):
    if a % b == 0 or a >= 0:
        return a // b
    else:
        return -((-a) // b) - 1


M = max(A)
m = min(A)
D = Y - X
r = X * A[0] % D
for i in range(N):
    if X * A[i] % D != r:
        print(-1)
        exit()

P = D * floor(Y * m - r, D) + r
if P < X * M:
    print(-1)
    exit()

ans = 0
for i in range(N):
    ans += (P - X * A[i]) // D
print(ans)
