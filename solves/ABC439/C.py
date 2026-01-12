import math

N = int(input())

numbers = {}
stop = int(math.sqrt(10**7))
for i in range(1, stop + 1):
    j = i + 1
    while True:
        n = i**2 + j**2
        if n > N:
            break
        if n in numbers.keys():
            numbers[n] += 1
        else:
            numbers[n] = 1
        j += 1

length = 0
good_n = []
for key in numbers.keys():
    if numbers[key] == 1:
        good_n.append(key)
        length += 1
good_n.sort()
print(length)
print(*good_n)
