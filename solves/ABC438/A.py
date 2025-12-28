D, F = map(int, input().split())

a = (D - F) // 7
if (D - F) % 7 != 0:
    a += 1
F += a * 7
ans = F % D
if ans == 0:
    ans = 7
print(ans)
