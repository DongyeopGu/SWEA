dt = [(1,0), (0,1), (-1,0), (0,-1)]
def sol(x,y,b,cnt=1):
    global max_r
    if max_r < cnt:
        max_r = cnt
    visit[x][y] = 1
    for d in dt:
        dx, dy = x + d[0], y + d[1]
        if not (0 <= dx < n and 0 <= dy < n) or visit[dx][dy] == 1:
            continue
        if Map[x][y] > Map[dx][dy]:
            sol(dx,dy,b,cnt+1)
        elif b > 0 and Map[x][y] > Map[dx][dy] - k:
            temp = Map[dx][dy]
            Map[dx][dy] = Map[x][y] - 1
            sol(dx,dy,0,cnt+1)
            Map[dx][dy] = temp
    visit[x][y] = 0
for t in range(int(input())):
    n, k = map(int, input().split())
    Map = [list(map(int, input().split()))for _ in range(n)]
    visit = [[0 for _ in range(n)]for _ in range(n)]
    top_height = 0
    top_idx = []
    for i in range(n):
        if top_height < max(Map[i]):
            top_height = max(Map[i])
    for i in range(n):
        for j in range(n):
            if Map[i][j] == top_height:
                top_idx.append((i,j))
    max_r = 0
    for top in top_idx:
        sol(top[0],top[1],1)
    print(f"#{t+1} {max_r}")