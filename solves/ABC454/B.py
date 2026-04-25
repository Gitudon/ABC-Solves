N, M = map(int, input().split())
F = list(map(int, input().split()))

huku = [0] * M
for i in range(N):
    huku[F[i] - 1] += 1

q_1 = 0
for i in range(M):
    if huku[i] == 1:
        q_1 += 1
if q_1 == N:
    print("Yes")
else:
    print("No")

ans = "Yes"
for i in range(M):
    if huku[i] == 0:
        ans = "No"
print(ans)
