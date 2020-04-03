# dt = [(1,0), (-1,0), (0,1), (0,-1)]
# def xy(i,j):
#     return 0 <= i < n and 0<= j < n and (maze[i][j] == 0 or maze[i][j]==3)
# def solv(i,j):
#     global cnt
#     q.append([i,j])
#     visit[i][j] = 1
#     while q:
#         x, y = q.pop(0)
#         for idx in range(4):
#             nx = x + dt[idx][0]
#             ny = y + dt[idx][1]
#             if xy(nx,ny) and [nx, ny] and visit[nx][ny]==0:
#                     q.append([nx,ny])
#                     visit[nx][ny]=1
#                     d[nx][ny] = d[x][y] + 1
#                     if maze[nx][ny]==3:
#                         cnt = d[nx][ny] - 1
#                         return

# for t in range(int(input())):
#     n = int(input())
#     maze = [list(map(int, input()))for _ in range(n)]
#     visit = [[0 for _ in range(n)]for _ in range(n)]
#     q = []
#     d =[[0 for _ in range(n)]for _ in range(n)]
#     cnt = 0
#     for i in range(n):
#         for j in range(n):
#             if maze[i][j] == 2:
#                 a, b = i, j
#                 break
#     solv(a,b)
#     print(f"#{t+1} {cnt}")

a = 9 
print(bin(a)[2:])