X = list(input())

X = sorted(X)

ans = ""
for i in range(len(X)):
    if X[i] != "0":
        ans += X[i]
        X.remove(X[i])
        break

for x in X:
    ans += x

print(ans)
