S = input()

ans = 0
for i in range(len(S)):
    if S[i] == "i" or S[i] == "j":
        ans += 1
print(ans)
