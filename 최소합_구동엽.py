dx, dy = [0,1], [1,0]
def dfs(x,y):
    global min_num, result
    visit[x][y] = 1
    if  result < min_num:
        return
    if x == n-1 and y == n-1:
        result = min_num
        return
    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
            min_num += a[nx][ny]
            dfs(nx,ny)
            visit[nx][ny] = 0
            min_num -= a[nx][ny]


for t in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    visit = [[0 for _ in range(n)]for _ in range(n)]
    min_num = a[0][0]
    result = 10000000
    dfs(0,0)
    print(f"#{t+1} {result}")