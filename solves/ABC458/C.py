S = input()

ans = 0
for i in range(len(S)):
    if S[i] == "C":
        mae = i
        ushiro = len(S) - 1 - i
        ans += min(mae, ushiro) + 1
print(ans)
