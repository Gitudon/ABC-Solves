W, B = map(int, input().split())
ans = 1

buf = B
W *= 1000
while B <= W:
    B += buf
    ans += 1
print(ans)
