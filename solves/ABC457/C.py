N, K = map(int, input().split())
L = [0] * N
A = [[]] * N
for i in range(N):
    buf = list(map(int, input().split()))
    L[i] = buf[0]
    A[i] = buf[1:]
C = list(map(int, input().split()))

B_len = 0
for i in range(N):
    husoku = K - B_len
    buf = L[i] * C[i]
    if husoku > buf:
        B_len += buf
    else:
        idx = husoku % L[i] - 1
        print(A[i][idx])
        break
