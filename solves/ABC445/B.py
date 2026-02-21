N = int(input())
S = [0] * N
for i in range(N):
    S[i] = input()

m = 0
for i in range(N):
    m = max(len(S[i]), m)

for i in range(N):
    k = (m - len(S[i])) // 2
    print("." * k + S[i] + "." * k)
