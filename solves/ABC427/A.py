S = input()
S = S[: (len(S) + 1) // 2 - 1] + S[(len(S) + 1) // 2 :]
print(S)
