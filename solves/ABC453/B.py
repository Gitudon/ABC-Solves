T, X = map(int, input().split())
A = list(map(int, input().split()))

last_saved = A[0]
print(0, last_saved)
for i in range(1, T + 1):
    if abs(last_saved - A[i]) >= X:
        last_saved = A[i]
        print(i, last_saved)
