A = [[]] * 3
for i in range(3):
    A[i] = list(map(int, input().split()))

count = 0
for i in range(6):
    for j in range(6):
        for k in range(6):
            tmp = [A[0][i], A[1][j], A[2][k]]
            if tmp.count(4) == 1 and tmp.count(5) == 1 and tmp.count(6) == 1:
                count += 1

print(count / 6**3)
