# def solv(n,x=0,y=1,z=1):    # z == 파이프 상태 0 세로 1 가로 2 대각선
#     global cnt
#     cnt = 0
#     if x == n-1 and y == n-1:
#         cnt += 1
#         return 
#     else:
#         if z == 0:
#             if x+1 < n and a[x+1][y] == 0:
#                 solv(n,x+1,y,0)
#             if (x+1 < n and y+1 < n) and a[x+1][y] == 0 and a[x+1][y+1] == 0 and a[x][y+1] == 0:
#                 solv(n,x+1,y+1,2)
#         elif z == 1:
#             if y+1 < n and a[x][y+1] == 0:
#                 solv(n,x,y+1,1)
#             if (x+1 < n and y+1 < n) and a[x+1][y] == 0 and a[x+1][y+1] == 0 and a[x][y+1] == 0:
#                 solv(n,x+1,y+1,2)
#         elif z == 2:
#             if y+1 < n and a[x][y+1] == 0:
#                 solv(n,x,y+1,1)
#             if x+1 < n and a[x+1][y] == 0:
#                 solv(n,x+1,y,0)
#             if (x+1 < n and y+1 < n) and a[x+1][y] == 0 and a[x+1][y+1] == 0 and a[x][y+1] == 0:
#                 solv(n,x+1,y+1,2)
    
    

# n = int(input())
# a = [list(map(int, input().split()))for _ in range(n)]
# cnt = 0
# solv(n)
# print(cnt)



# for t in range(10):
#     n = int(input())
#     a = [list(map(str, input()))for _ in range(8)]
#     a += [[a[i][j]for i in range(8)]for j in range(8)]
#     c = 0
#     for i in range(16):
#         for j in range(9-n):
#             if a[i][j:j+n] == list(reversed(a[i][j:j+n])):
#                 c += 1
#     print(f"#{t+1} {c}")
# def pal(a,n):
#     for i in range(100):
#         for j in range(100-n):
#             for k in range(n//2):
#                 if a[i][j+k] != a[i][j+n-1-k]:
#                     break
#                 elif k + 1 == n//2:
#                     return n
#             for k in range(n//2):
#                 if a[j+k][i] != a[j+n-1-k][i]:
#                     break
#                 elif k + 1 == n//2:
#                     return n
#     return 0
# for _ in range(10):
#     print(f"#{input()}",end=' ')
#     a = [input() for _ in range(100)]
#     for i in range(50,0,-1):
#         n = pal(a,i)
#         if n:
#             print(n)
#             break
for t in range(int(input())):
    n, m = map(int, input().split())
    a = [list(map(int, input().split()))for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            b = a[i][j]
            c = b
            for k in range(1, b+1):
                if i+k < n:
                    c += a[i+k][j]
                if i-k >= 0:
                    c += a[i-k][j]
                if j+k < m:
                    c += a[i][j+k]
                if j-k >= 0:
                    c += a[i][j-k]
            if result < c:
                result = c
    print(f"#{t+1} {result}")
