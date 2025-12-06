N = int(input())
A = list(map(int, input().split()))

domino = [False] * N
domino[0] = True
current = A[0] + 1
for i in range(1, N):
    if i + 1 < current:
        domino[i] = True
        current = max(current, i + 1 + A[i])
    else:
        break

print(sum(domino))
