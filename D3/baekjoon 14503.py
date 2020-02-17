delta = [(-1,0),(0,1),(1,0),(0,-1)]
g_l = [(0,-1),(1,0),(0,1),(-1,0)]   # 왼쪽부터 탐색위해

n, m = map(int,input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split()))for _ in range(n)]
room[r][c] = 2  #현재 위치 청소표시

while True:
    x = r + g_l[d][0]
    y = c + g_l[d][1]
    d += 1
    if d> 3:
        d = 0
    if room[x][y] == 0:
        room[x][y] = 2
    if (room[x][y] == 1 or room[x][y] == 2) and (room[x-delta[d][0]][y-delta[d][1]] == 0 or room[x-delta[d][0]][y-delta[d][1]] == 2):
        x -= delta[d][0]
        y -= delta[d][1]
    if (room[x][y] == 1 or room[x][y] == 2) and room[x-delta[d][0]][y-delta[d][1]] == 1:
        break
print(room)    
