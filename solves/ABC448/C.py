N, Q = map(int, input().split())
A = list(map(int, input().split()))
A_dash = sorted(A)
A_map = {}
for a in A:
    if a in A_map:
        A_map[a] += 1
    else:
        A_map[a] = 1


for _ in range(Q):
    K = int(input())
    B = list(map(int, input().split()))
    B_map = {}
    for b in B:
        res = A[b - 1]
        if res in B_map:
            B_map[res] += 1
        else:
            B_map[res] = 1
    for b in B_map.keys():
        A_map[b] -= B_map[b]
    i = 0
    while True:
        ans = A_dash[i]
        if A_map[ans] != 0:
            # print(f"ans: {ans}")
            print(ans)
            for b in B_map.keys():
                A_map[b] += B_map[b]
            break
        else:
            i += 1
