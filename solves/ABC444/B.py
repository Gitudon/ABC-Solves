N, K = map(int, input().split())


def digit_sum(n):
    buf = 0
    n = str(n)
    for i in range(len(n)):
        buf += int(n[i])
    return buf


ans = 0
for i in range(1, N + 1):
    if digit_sum(i) == K:
        ans += 1

print(ans)
