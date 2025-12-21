H, W, N = map(int, input().split())

A = [0] * H
for i in range(H):
    A[i] = list(map(int, input().split()))

B = [0] * N
for i in range(N):
    B[i] = int(input())

ans = 0
for i in range(H):
    buf = 0
    for j in range(W):
        if A[i][j] in B:
            buf += 1
    ans = max(buf, ans)
print(ans)
