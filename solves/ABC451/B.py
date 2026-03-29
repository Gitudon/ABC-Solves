N, M = map(int, input().split())

konki = [0] * M
raiki = [0] * M

for _ in range(N):
    A, B = map(int, input().split())
    konki[A - 1] += 1
    raiki[B - 1] += 1

for i in range(M):
    print(raiki[i] - konki[i])
