<<<<<<< HEAD
def pipe(n, x=0, y=1, idx=0):
    dx = [0,1,1]           # x좌표 idx 뒤부분
    dy = [1,0,1]            # y좌표 idx 앞부분
    cnt = 0
    if x == n - 1 and y == n - 1:
        return 1
    for i in range(3):
        if i + idx == 1:
            continue
        c_x = dx[i] + x
        c_y = dy[i] + y
        if  c_x >= n or c_y >= n or a[c_x][c_y]:
            continue
        if idx == 2 and (a[x][y+1] or a[x+1][y]):
            continue
        cnt += pipe(n,c_x,c_y,i)
    return cnt




n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
print(pipe(n))

# dx, dy = (0, 1, 1), (1, 0, 1)
# n = int(input())
# a = [list(map(int, input().split())) for _ in range(n)]

# def solve(x, y, z):
#     res = 0
#     if x == n-1 and y == n-1:
#         return 1
#     for i in range(3):
#         if i+z == 1:
#             continue
#         nx, ny = x+dx[i], y+dy[i]
#         if nx >= n or ny >= n or a[nx][ny]:
#             continue
#         if i == 2 and (a[x][y+1] or a[x+1][y]):
#             continue
#         res += solve(nx, ny, i)
#     return res

# print(solve(0, 1, 0))
=======
a = list(map(str, input().upper()))
b = list(set(a))
cnt = []
for i in b:
    cnt.append(a.count(i))
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(b[cnt.index(max(cnt))])
 
>>>>>>> 67ca1bc789e8cf5dac6b86a91518df8702d12553
