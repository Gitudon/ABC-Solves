N = int(input())
L = [0] * N
A = [[]] * N
for i in range(N):
    buf = list(map(int, input().split()))
    L[i] = buf[0]
    A[i] = buf[1:]

X, Y = map(int, input().split())
print(A[X - 1][Y - 1])
