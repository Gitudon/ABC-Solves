N, Q = map(int, input().split())
A = list(map(int, input().split()))
A_dash = sorted(A)[:6]

for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    A_dash_copy = A_dash.copy()
    for b in B:
        res = A[b - 1]
        if res in A_dash_copy:
            A_dash_copy.remove(res)
    print(min(A_dash_copy))
