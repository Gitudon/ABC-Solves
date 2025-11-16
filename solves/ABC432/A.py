li = list(map(int, input().split()))

li = sorted(li, reverse=True)
print(100 * li[0] + 10 * li[1] + li[2])
