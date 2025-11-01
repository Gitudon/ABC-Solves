A, B, C, D = map(int, input().split())

ans = "No"
if C >= A:
    if D < B:
        ans = "Yes"
print(ans)
