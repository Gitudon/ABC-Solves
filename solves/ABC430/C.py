from bisect import *

N, A, B = map(int, input().split())
S = input()

a_ruisekiwa = [0] * (N + 1)
b_ruisekiwa = [0] * (N + 1)

for i in range(1, N + 1):
    if S[i - 1] == "a":
        a_ruisekiwa[i] = a_ruisekiwa[i - 1] + 1
        b_ruisekiwa[i] = b_ruisekiwa[i - 1]
    else:
        b_ruisekiwa[i] = b_ruisekiwa[i - 1] + 1
        a_ruisekiwa[i] = a_ruisekiwa[i - 1]

ans = 0
for l in range(N):
    min_r_for_a = bisect_left(a_ruisekiwa, a_ruisekiwa[l] + A, l + 1, N + 1)
    max_r_for_b = bisect_right(b_ruisekiwa, b_ruisekiwa[l] + B - 1, l + 1, N + 1) - 1
    if min_r_for_a <= max_r_for_b:
        ans += max_r_for_b - min_r_for_a + 1

print(ans)
