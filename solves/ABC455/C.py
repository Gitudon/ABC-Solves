N, K = map(int, input().split())
A = list(map(int, input().split()))
A = sorted(A)
ans = sum(A)

kiroku = []
buf = 1
focus = A[0]
for i in range(1, N):
    if A[i] == focus:
        buf += 1
    else:
        kiroku.append(focus * buf)
        focus = A[i]
        buf = 1
kiroku.append(focus * buf)

kiroku = sorted(kiroku, reverse=True)
for i in range(min(K, len(kiroku))):
    ans -= kiroku[i]

print(ans)
