M, D = map(int, input().split())

if M % 2 == 0:
    print("No")
elif M == 11:
    print("No")
elif M == 1:
    if D == 7:
        print("Yes")
    else:
        print("No")
else:
    if M == D:
        print("Yes")
    else:
        print("No")
