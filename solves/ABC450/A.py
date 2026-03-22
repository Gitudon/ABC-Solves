N = int(input())

ans = ""

for i in range(N, 0, -1):
    ans += str(i)
    ans += ","

print(ans[:-1])
