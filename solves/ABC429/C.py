N = int(input())
A = list(map(int, input().split()))
infty = int(2e5)
Arr = [0] * infty
ans = 0

for i in range(N):
    X = A[i]
    Arr[X - 1] += 1

for i in range(N):
    ans += Arr[i] * (Arr[i] - 1) * (N - Arr[i]) // 2

print(ans)
