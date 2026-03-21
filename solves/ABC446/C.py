from collections import deque

T = int(input())

for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    q = deque()
    for i in range(N):
        # morning
        for _ in range(A[i]):
            q.append(i)
        # noon
        for _ in range(B[i]):
            q.popleft()
        # night
        while True:
            try:
                egg = q.popleft()
                if egg != i - D:
                    q.appendleft(egg)
                    break
            except:
                break
    print(len(q))
