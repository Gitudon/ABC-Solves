N = int(input())
L = list(map(int, input().split()))

ans = -(10**10)


def sign(n):
    if n > 0:
        return 1
    else:
        return 0


def bit_full_search(cnt, num, current):
    global ans
    if cnt == N:
        ans = max(ans, num)
        return
    # 正の方向へ進む
    positive = current + L[cnt]
    # 原点を通過した
    if sign(current) != sign(positive):
        bit_full_search(cnt + 1, num + 1, positive)
    else:
        bit_full_search(cnt + 1, num, positive)
    # 負の方向へ進む
    negative = current - L[cnt]
    # 原点を通過した
    if sign(current) != sign(negative):
        bit_full_search(cnt + 1, num + 1, negative)
    else:
        bit_full_search(cnt + 1, num, negative)


bit_full_search(0, 0, 0.5)
print(ans)
