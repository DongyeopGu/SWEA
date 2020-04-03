dt = [(1,0), (-1,0), (0,1), (0,-1)]
def xy(i,j):
    return 0 <= i < row and 0 <= j < col and Map[i][j] == 'L'

def solv(x,y):
    q.append([x,y])
    dist = [[0 for _ in range(col)]for _ in range(row)]
    dist[x][y] = 1
    result = 0
    while q:
        i, j = q.pop(0)
        for idx in dt:
            nx = i + idx[0]
            ny = j + idx[1]
            if xy(nx,ny) and dist[nx][ny] == 0:
                dist[nx][ny] = dist[i][j] + 1
                result = max(result, dist[nx][ny]) 
                q.append([nx,ny])
    return result - 1

row, col = map(int, input().split())
Map = [list(map(str, input()))for _ in range(row)]
visit = [[0 for _ in range(col)]for _ in range(row)]
q = []
cnt = 0
for i in range(row):
    for j in range(col):
        if Map[i][j] == 'L':
            cnt = max(cnt, solv(i,j))
print(cnt)