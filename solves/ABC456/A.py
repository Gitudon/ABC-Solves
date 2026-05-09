X = int(input())

flag = False
for i in range(1, 7):
    for j in range(1, 7):
        for k in range(1, 7):
            if i + j + k == X:
                flag = True

if flag:
    print("Yes")
else:
    print("No")
