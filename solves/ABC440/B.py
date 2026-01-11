N = int(input())
T = list(map(int, input().split()))

sorted_T = sorted(T)
ans = []
for i in range(3):
    for j in range(N):
        if T[j] == sorted_T[i]:
            ans.append(j + 1)
            break

print(*ans)
