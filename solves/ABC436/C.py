N, M = map(int, input().split())

ans = 0
put_masu = set()

for _ in range(M):
    R, C = map(int, input().split())
    R -= 1
    C -= 1
    if (
        (R, C) not in put_masu
        and (R + 1, C) not in put_masu
        and (R, C + 1) not in put_masu
        and (R + 1, C + 1) not in put_masu
    ):
        ans += 1
        put_masu.add((R, C))
        put_masu.add((R + 1, C))
        put_masu.add((R, C + 1))
        put_masu.add((R + 1, C + 1))
print(ans)
