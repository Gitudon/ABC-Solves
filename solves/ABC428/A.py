S, A, B, X = map(int, input().split())

ans = S * A * (X // (A + B))
nokori = X % (A + B)
if nokori >= A:
    ans += S * A
else:
    ans += S * nokori
print(ans)
