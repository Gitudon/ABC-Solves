H, W, Q = map(int, input().split())

chocolate = [[True] * W for _ in range(H)]

for _ in range(Q):
    number, integer = map(int, input().split())
    count = 0
    if number == 1:
        for i in range(integer):
            for j in range(W):
                if chocolate[H - integer + i][j]:
                    count += 1
                    chocolate[H - integer + i][j] = False
        H -= integer
    else:
        for i in range(H):
            for j in range(integer):
                if chocolate[i][W - integer + j]:
                    count += 1
                    chocolate[i][W - integer + j] = False
        W -= integer
    print(count)
