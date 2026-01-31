volume = 0
playing = 0

Q = int(input())
for _ in range(Q):
    A = int(input())
    if A == 1:
        volume += 1
    elif A == 2:
        if volume >= 1:
            volume -= 1
    else:
        playing = not playing
    if playing and volume >= 3:
        print("Yes")
    else:
        print("No")
