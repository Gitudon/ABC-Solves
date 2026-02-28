S = input()
dictionary = {}

for s in S:
    if s not in dictionary:
        dictionary[s] = 1
    else:
        dictionary[s] += 1

max_value = 0
for key in dictionary.keys():
    if max_value < dictionary[key]:
        max_value = dictionary[key]

ans = ""
for s in S:
    if dictionary[s] != max_value:
        ans += s

print(ans)
