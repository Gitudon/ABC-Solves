N = int(input())
A = list(map(int, input().split()))

ans = 0
for l in range(N):
    for r in range(l, N):
        sum_A = 0
        for i in range(l, r + 1):
            sum_A += A[i]
        flag = True
        for i in range(l, r + 1):
            if sum_A % A[i] == 0:
                flag = False
        if flag:
            ans += 1

print(ans)
