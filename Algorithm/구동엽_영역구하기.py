from sys import*
setrecursionlimit(10**6)

dt = ([1, 0], [-1, 0], [0, 1], [0, -1])
def solv(y,x):
    global cnt
    visit[y][x] = 1
    cnt += 1
    for i in range(4):
        nx = x + dt[i][0]
        ny = y + dt[i][1]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[ny][nx] == 0 and visit[ny][nx]==0:
                solv(ny,nx)
            
m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)]for _ in range(m)]
for i in range(k):
    a, b, c, d = map(int, input().split())
    for x in range(a,c):
        for y in range(b,d):
            arr[y][x] = 1
arr = list(reversed(arr))
visit = [[0 for _ in range(n)]for _ in range(m)]
result = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and visit[i][j] == 0:
            cnt = 0
            solv(i,j)
            result.append(cnt)

print(len(result))
print(' '.join(map(str, sorted(result))))