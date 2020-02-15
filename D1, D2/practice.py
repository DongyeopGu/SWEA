# for t in range(int(input())):
#     n = int(input())
#     a = [[0 for _ in range(n)]for _ in range(n)]
#     dx = [0,1,0,-1]
#     dy = [1,0,-1,0]
#     i = 0
#     j = 0
#     idx = 0
#     cnt = 0
#     while cnt < n**2:
#         if j+ dy[idx] > n-1 or i + dx[idx] > n-1 or j+ dy[idx] < 0 or i + dx[idx] < 0 or a[i+dx[idx]][j+dy[idx]]!=0:
#             idx += 1
#             if idx > 3:
#                 idx = 0
#         cnt += 1
#         a[i][j] = cnt
#         i = i + dx[idx]
#         j = j + dy[idx]
#     print(f"#{t+1}")
#     for i in range(n):
#         print(' '.join(map(str, a[i])))

n = int(input())
switch = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    student = list(map(int, input().split()))
    if student[0] == 1:
        i = student[1] - 1
        for a in range(i,n,i+1):
            switch[a] = 1 - switch[a]
    else:
        i = student[1] - 1
        switch[i] = 1- switch[i]
        for a in range(1,n//2+1):
            if switch[i-a] == switch[i+a] and 0<=i-a and i+a<n:
                switch[i-a] = 1 - switch[i-a]
                switch[i+a] = 1 - switch[i+a]
                
                
            else:
                break
cnt = 0
for i in range(n):
    print(switch[i],end=' ')
    if cnt>0 and cnt%20==0:
        print()