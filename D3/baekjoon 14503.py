dt = [(-1,0),(0,1),(1,0),(0,-1)]   # 북, 동, 남, 서
def leftdir(d):                    # 왼쪽 탐색 index 만들기 위해
    if d == 0:
        return 3
    else:
        return d - 1

n, m = map(int,input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split()))for _ in range(n)]
check = 0
x = r
y = c
while True:
    d = d % 4
    if check == 4:                          # 4가지 방향 탐색 후
        bx = x - dt[d][0]          # 뒤로 한칸 가서
        by = y - dt[d][1]          
        if room[bx][by] == 1:               # 벽이면 break
            break
        else: 
            x = bx
            y = by
            check = 0
    if room[x][y] == 0:                     # 먼저 청소기 놓은곳 2로 변경
        room[x][y] = 2
    nd = leftdir(d)
    nx = x + dt[nd][0]
    ny = y + dt[nd][1]
    if room[nx][ny] == 0:                   # 왼쪽이 0 일때 x, y 변경
        x = nx
        y = ny
        d = leftdir(d)
        check = 0
    else:                 
        d = leftdir(d)
        check += 1
cnt = 0
for i in range(n):
    for j in range(m):
        if room[i][j] == 2:
            cnt += 1
print(cnt)
