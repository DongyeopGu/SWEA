# def check(a):
#     h = a[0]
#     i = 1
#     count = 1
#     while i < n:
#         if h == a[i]:
#             i += 1
#             count += 1
#             continue
#         if h == a[i] - 1:
#             if l > count:           
#                 return 0
#             else:                   
#                 h = a[i]
#                 i += 1
#                 count = 1
#                 continue
#         elif h == a[i] + 1:
#             for idx in range(l):
#                 if i + idx > n-1:
#                     return 0
#                 if a[i] != a[i+idx]:
#                     return 0
                
#             if i + l >= n:
#                 return 1
#             else:
#                 count = 0
#                 i += l
#                 h = a[i-1]
#         else:
#             return 0
#     return 1
# n, l = map(int, input().split())
# a = [list(map(int, input().split()))for _ in range(n)]
# a += [[a[i][j]for i in range(n)] for j in range(n)]
# cnt = 0
# for i in range(2*n):
#     cnt += check(a[i])
# print(cnt)

# def slope(i, c):
#     global ans
#     cnt = 1
#     for j in range(0, N-1):
#         d = a[i][j+1]-a[i][j] if c else a[j+1][i]-a[j][i]
#         if d == 0:
#             cnt += 1
#         elif d == 1 and cnt >= L:
#             cnt = 1
#         elif d == -1 and cnt >= 0:
#             cnt = -L+1
#         else:
#             return
#     if cnt >= 0:
#         ans += 1

# def solve():
#     for i in range(N):
#         slope(i, 1)
#         slope(i, 0)
#     print(ans)

# N, L = map(int, input().split())
# a = [list(map(int, input().split())) for _ in range(N)]
# ans = 0
# solve()


# 출처: https://rebas.kr/788 [PROJECT REBAS]



def check(a):
    cnt = 1
    for j in range(n-1):
        dif = a[j+1] - a[j]
        if dif == 0:
            cnt += 1
        elif dif == 1 and cnt >= l:
            cnt = 1
        elif dif == -1 and cnt >= 0:
            cnt = -l+1
        else:
            return 0
    else: 
        if cnt >= 0:
            return 1
n, l = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(n)]
a_1= [[a[i][j]for i in range(n)] for j in range(n)]
result = 0
for i in range(n):
    result += check(a[i])
    result += check(a_1[i])
print(result)