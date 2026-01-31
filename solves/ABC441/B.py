N, M = map(int, input().split())
S = input()
T = input()
Q = int(input())

for _ in range(Q):
    w = input()
    takahashi = True
    aoki = True
    for char in w:
        if char not in S:
            takahashi = False
        if char not in T:
            aoki = False
    if takahashi:
        if not aoki:
            print("Takahashi")
        else:
            print("Unknown")
    else:
        if not aoki:
            print("Unknown")
        else:
            print("Aoki")
