S = input()
T = input()


def decompose(S):
    T = ""
    v = []
    cnt = 0
    for s in S:
        if s == "A":
            cnt += 1
        else:
            T += s
            v.append(cnt)
            cnt = 0
    v.append(cnt)
    return T, v


ss, sv = decompose(S)
ts, tv = decompose(T)

if ss != ts:
    print(-1)
    exit()

ans = 0
for i in range(len(sv)):
    ans += abs(sv[i] - tv[i])
print(ans)
