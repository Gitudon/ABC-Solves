N, K = map(int, input().split())

mame = 0
ans = 0
while True:
    mame += N
    if mame >= K:
        print(ans)
        break
    ans += 1
    N += 1
