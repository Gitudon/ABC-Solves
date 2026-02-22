N, M = map(int, input().split())

selected = set()

for _ in range(N):
    L = int(input())
    X = list(map(int, input().split()))
    water = True
    for x in X:
        if x not in selected:
            print(x)
            selected.add(x)
            water = False
            break
    if water:
        print(0)
