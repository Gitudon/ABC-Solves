N = int(input())
A = list(map(int, input().split()))

Q = []
for a in A:
    Q.append(a)
    if len(Q) >= 4:
        if Q[-1] == Q[-2] == Q[-3] == Q[-4]:
            for _ in range(4):
                Q.pop()

print(len(Q))
