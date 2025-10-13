N = int(input())


def A(N):
    if N == 0:
        return 1
    a = A(N - 1)
    str_N = str(a)
    f = 0
    for s in str_N:
        f += int(s)
    if N == 1:
        f -= 1
    return a + f


print(A(N))
