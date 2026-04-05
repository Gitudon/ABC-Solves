from heapq import heappop, heappush

que = []
ans = 0
Q = int(input())

for _ in range(Q):
    num, h = map(int, input().split())
    if num == 1:
        heappush(que, h)
        ans += 1
    else:
        while que and que[0] <= h:
            heappop(que)
            ans -= 1
    print(ans)
