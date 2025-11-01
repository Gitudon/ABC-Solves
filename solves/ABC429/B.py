N, M = map(int, input().split())
A = list(map(int, input().split()))

sum_A = 0
for i in range(N):
    sum_A += A[i]

ans = "No"
for i in range(N):
    if sum_A - A[i] == M:
        ans = "Yes"
print(ans)
