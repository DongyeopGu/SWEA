def sol(a, s):
    global result
    if a == n:
        if result > s:
            result = s
        return
    if result < s:
        return
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            sol(a+1, s + arr[a][i])
            visit[i] = 0

for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    result = 1111111111111
    visit = [0] * n
    sol(0,0)
    print(f"#{t+1} {result}")