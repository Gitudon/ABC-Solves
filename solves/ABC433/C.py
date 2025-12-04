S = input()

assyuku = []
focus = S[0]
current = 1
for i in range(1, len(S)):
    if S[i] == focus:
        current += 1
    else:
        assyuku.append((focus, current))
        focus = S[i]
        current = 1
assyuku.append((focus, current))

ans = 0
if len(assyuku) == 1:
    print(ans)
else:
    for i in range(len(assyuku) - 1):
        if int(assyuku[i][0]) + 1 == int(assyuku[i + 1][0]):
            ans += min(assyuku[i][1], assyuku[i + 1][1])
    print(ans)
