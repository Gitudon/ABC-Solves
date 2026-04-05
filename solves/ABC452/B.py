H, W = map(int, input().split())

for i in range(H):
    ans = ""
    for j in range(W):
        if i == 0 or i == H - 1:
            ans += "#"
        else:
            if j == 0 or j == W - 1:
                ans += "#"
            else:
                ans += "."
    print(ans)
