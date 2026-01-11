N = int(input())


def take_sum_of_each_digit(n):
    sum = 0
    for s in str(n):
        sum += int(s) ** 2
    return sum


appeared = set()
while True:
    if N in appeared:
        print("No")
        break
    if N == 1:
        print("Yes")
        break
    appeared.add(N)
    N = take_sum_of_each_digit(N)
