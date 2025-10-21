N, K = map(int, input().split())
S = input()

strings = {}
for i in range(N - K + 1):
    if i == N - K:
        s = S[i:]
    else:
        s = S[i : i + K]
    if s not in strings:
        strings[s] = 1
    else:
        strings[s] += 1

x = max(strings.values())
ans = []
for key in strings.keys():
    if strings[key] == x:
        ans.append(key)

print(x)
print(*sorted(ans))
