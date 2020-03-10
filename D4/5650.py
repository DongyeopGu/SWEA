# 방향 상 좌 하 우
dx = (-1, 0, 1, 0)
dy = (0, -1, 0, 1)
# 1번 블록 : 상 > 하, 좌 > 상, 하 > 우, 우 > 좌
block = ((2, -1, 1, -2), (3, 1, -2, -2), (1, 2, -2, -1), (2, 2, -1, -3), (2, 2, -2, -2))

def sol(x,y,d):
    global result, n
    cnt = 0
    nx = x
    ny = y
    while True:
        nx += dx[d]
        ny += dy[d]
        if not (n > nx >= 0 and n > ny >= 0):       # 벽 만났을 때 튕김(방향은 반대로)
            d = (d + 2) % 4
            cnt += 1
        else:       
            if game_board[nx][ny] == -1 or (nx == x and ny == y):
                result = max(cnt, result)
                return
            elif game_board[nx][ny] == 0:
                continue
            elif 0<game_board[nx][ny] < 6:                # 블록 만났을 때
                d += block[game_board[nx][ny]-1][d]
                cnt += 1
            else:
                for a, b in warmhole[game_board[nx][ny]]:   # 웜홀 만났을때 인덱스 변경
                    if nx != a or ny != b:
                        nx = a
                        ny = b
                        break

for t in range(int(input())):
    n = int(input())
    game_board = [list(map(int, input().split()))for _ in range(n)]
    warmhole = {6:[],7:[],8:[],9:[],10:[]}
    for i in range(n):
        for j in range(n):
            if game_board[i][j] > 5:
                warmhole[game_board[i][j]].append((i,j))
    result = 0
    
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                for k in range(4):
                    sol(i,j,k)
    print(f"#{t+1} {result}")