T = int(input())


def is_overlap(A, B, X, Y):
    return X <= B and A <= Y


for _ in range(T):
    N, H = map(int, input().split())
    t = [0] * N
    l = [0] * N
    u = [0] * N
    for i in range(N):
        t[i], l[i], u[i] = map(int, input().split())
    ans = "Yes"
    down = H
    up = H
    current_time = 0
    for i in range(N):
        down -= t[i] - current_time
        up += t[i] - current_time
        if not is_overlap(down, up, l[i], u[i]):
            ans = "No"
            break
        if l[i] < down and down <= u[i] <= up:
            up = u[i]
        elif down <= l[i] and u[i] <= up:
            down = l[i]
            up = u[i]
        elif down <= l[i] and up < u[i]:
            down = l[i]
        current_time = t[i]
    print(ans)
