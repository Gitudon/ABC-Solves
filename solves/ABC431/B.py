X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())

parts = set()

for _ in range(Q):
    P = int(input()) - 1
    if P not in parts:
        parts.add(P)
        X += W[P]
    else:
        parts.remove(P)
        X -= W[P]
    print(X)
