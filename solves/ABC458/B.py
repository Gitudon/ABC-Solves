H, W = map(int, input().split())

ans = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        cnt = 0
        for k in range(H):
            for l in range(W):
                if abs(i - k) + abs(j - l) == 1:
                    cnt += 1
        ans[i][j] = cnt

for i in range(H):
    print(*ans[i])
