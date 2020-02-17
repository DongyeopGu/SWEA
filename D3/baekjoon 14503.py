import sys
sys.setrecursionlimit(30000)


dt = [(0,-1),(1,0),(0,1),(-1,0)]   # 왼쪽부터 탐색위해
def clean(x,y,d,check, cnt):
    d = d%4
    if room[x][y] == 0:
        room[x][y] = 2
        cnt += 1
    nx, ny = x + dt[d][0], y + dt[d][0]
    if room[nx][ny] == 0:
        x = nx
        y = ny
        return clean(x,y,d+3,check,cnt)
    elif (room[nx][ny] == 1 or room[nx][ny] == 2) and check <3:
        return clean(nx,ny,d+3,check+1,cnt)
    elif (room[nx][ny] == 1 or room[nx][ny] == 2) and check == 3:
        if room[x+dt[(d+2)%4][0]][y+dt[(d+2)%4][1]] != 1:
            nx += dt[(d+2)%4][0]
            ny += dt[(d+2)%4][1]
            return clean(nx,ny,d+3,0,cnt)
        if room[x+dt[(d+2)%4][0]][y+dt[(d+2)%4][1]] == 1:
            return cnt
n, m = map(int,input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split()))for _ in range(n)]
check = 0
cnt = 0
result = clean(r,c,d,check,cnt)
print(result)
