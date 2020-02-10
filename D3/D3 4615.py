# 4615. 오셀로
def limit(a, b, n):
    if a >= 0 and a < n and b >= 0 and b < n:
        return True
    else:
        return False

for t in range(int(input())):
    N, M = map(int, input().split())
    data = [[0] * N for _ in range(N)]
    data[N // 2 - 1][N // 2] = 1
    data[N // 2][N // 2 - 1] = 1
    data[N // 2 - 1][N // 2 - 1] = 2
    data[N // 2][N // 2] = 2
  
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
  
    for _ in range(M):
        a, b, stone = map(int, input().split())
        x = a - 1
        y = b - 1
        data[x][y] = stone
        for i in range(8):
            cnt = 0
            next_x = x + dx[i]
            next_y = y + dy[i]
            while limit(next_x, next_y, N) and stone != data[next_x][next_y] and data[next_x][next_y] != 0:
                cnt += 1
                next_x = next_x + dx[i]
                next_y = next_y + dy[i]
  
            if limit(next_x, next_y, N) and data[next_x][next_y] == stone:
                next_x = x + dx[i]
                next_y = y + dy[i]
                for f in range(cnt):
                    data[next_x][next_y] = stone
                    next_x = next_x + dx[i]
                    next_y = next_y + dy[i]
                      
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                cnt1 += 1
            elif data[i][j] == 2:
                cnt2 += 1
    print(f"#{t+1} {cnt1} {cnt2}")
# 
# 
# 
# 
# # 4615. 오셀로
# def line_1(a,b,c):            
#     find = False
#     for i in range(b+1,N):
#         if othello[a][i] == 0:
#             find =False
#             break
#         if othello[a][i] == c:
#             find = True
#             break
#     if find:
#         for i in range(b+1,N):
#             if othello[a][i] == c or othello[a][i] == 0:
#                 break
#             othello[a][i] = c
#     return othello
# def line_2(a,b,c):       
#     find = False
#     for i in range(b-1,-1,-1):
#         if othello[a][i] == 0:
#             find =False
#             break
#         if othello[a][i] == c:
#             find = True
#             break
#     if find:
#         for i in range(b-1,-1,-1):
#             if othello[a][i] == c or othello[a][i] == 0:
#                 break
#             othello[a][i] = c
#     return othello

# def sero_1(a,b,c):
#     find = False
#     for i in range(a+1,N):
#         if othello[i][b] == 0:
#             find=False
#             break
#         if othello[i][b] == c:
#             find = True
#             break
#     if find:
#         for i in range(a+1,N):
#             if othello[i][b] == c or othello[i][b] == 0:
#                 break
#             othello[i][b] = c
#     return othello
# def sero_2(a,b,c):    
#     find = False
#     for i in range(a-1,-1,-1):
#         if othello[i][b] == 0:
#             find=False
#             break
#         if othello[i][b] == c:
#             find = True
#             break
#     if find:
#         for i in range(a-1,-1,-1):
#             if othello[i][b] == c or othello[i][b] == 0:
#                 break
#             othello[i][b] = c
#     return othello

# def diag_1(a,b,c):
#     find = False
#     for i in range(a+1,N):
#         for j in range(b+1,N):
#             if i - j == a - b:
#                 if othello[i][j] == 0:
#                     find = False
#                     break
#                 if othello[i][j] == c:
#                     find = True
#                     break
#     if find:
#         for i in range(a+1,N):
#             for j in range(b+1,N):
#                 if i - j == a - b:
#                     if othello[i][j] == c or othello[i][j] == 0:
#                         break
#                     othello[i][j] = c
#     return othello
# def diag_2(a,b,c):    
#     find = False
#     for i in range(a-1,-1,-1):
#         for j in range(b-1,-1,-1):
#             if i - j == a - b:
#                 if othello[i][j] == 0:
#                     find = False
#                     break
#                 if othello[i][j] == c:
#                     find = True
#                     break
#     if find:
#         for i in range(a-1,-1,-1):
#             for j in range(b-1,-1,-1):
#                 if i - j == a - b:
#                     if othello[i][j] == c or othello[i][j] == 0:
#                         break
#                     othello[i][j] = c
#     return othello
# def diag_3(a,b,c):
#     find = False
#     for i in range(a-1,-1,-1):
#         for j in range(b+1,N):
#             if i + j == a + b:
#                 if othello[i][j] == 0:
#                     find = False
#                     break
#                 if othello[i][j] == c:
#                     find = True
#                     break
#     if find:
#         for i in range(a-1,-1,-1):
#             for j in range(b+1,N):
#                 if i + j == a + b:
#                     if othello[i][j] == c or othello[i][j] == 0:
#                         break
#                     othello[i][j] = c
#     return othello
# def diag_4(a,b,c):
#     find = False
#     for i in range(a+1,N):
#         for j in range(b-1,-1,-1):
#             if i + j == a + b:
#                 if othello[i][j] == 0:
#                     find = False
#                     break
#                 if othello[i][j] == c:
#                     find = True
#                     break
#     if find:
#         for i in range(a+1,N):
#             for j in range(b-1,-1,-1):
#                 if i + j == a + b:
#                     if othello[i][j] == c or othello[i][j] == 0:
#                         break
#                     othello[i][j] = c
#     return othello

# for t in range(int(input())):
#     global N
#     N, M = map(int, input().split())
#     global othello 
#     othello= [[0 for _ in range(N)]for _ in range(N)]
#     othello[N//2-1][N//2-1:N//2+1] = [2, 1]
#     othello[N//2][N//2-1:N//2+1] = [1, 2]
#     for i in range(M):
#         put = list(map(int, input().split()))
#         othello[put[1]-1][put[0]-1] = put[2]
#         line_1(put[1]-1,put[0]-1,put[2])
#         line_2(put[1]-1,put[0]-1,put[2])
#         sero_1(put[1]-1,put[0]-1,put[2])
#         sero_2(put[1]-1,put[0]-1,put[2])
#         diag_1(put[1]-1,put[0]-1,put[2])
#         diag_2(put[1]-1,put[0]-1,put[2])
#         diag_3(put[1]-1,put[0]-1,put[2])
#         diag_4(put[1]-1,put[0]-1,put[2])
#     cnt = [0,0]
#     for i in range(N):
#         for j in range(N):
#             if othello[i][j] == 1:
#                 cnt[0] += 1
#             elif othello[i][j] == 2:
#                 cnt[1] += 1
#     print(f"#{t+1} {' '.join(map(str, cnt))}")
        