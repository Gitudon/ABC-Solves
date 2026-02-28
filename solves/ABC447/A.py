import math

N, M = map(int, input().split())

if M <= math.ceil(N / 2):
    print("Yes")
else:
    print("No")
