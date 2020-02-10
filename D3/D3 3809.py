# # 3809
# for t in range(int(input())):
#     n = int(input())
#     a = ''
#     while True:
#         a += ''.join(map(str, input().split()))
#         if len(a) == n:
#             break
#     print(a)
#     b = 0
#     c = 0
#     while True:
#         if str(b) not in a:
#             c = b
#             break
#         b += 1
#     print(f"#{t+1} {c}")

# 4789
# for t in range(int(input())):
#     a = list(map(int, input()))
#     cnt = 0
#     result = 0
#     for i in range(len(a)):
#         while True:
#             if cnt < i:
#                 cnt += 1
#                 result += 1
#             else:
#                 cnt += a[i]
#                 break
#     print(f"#{t+1} {result}")

# # 4371.
# for t in range(int(input())):
#     n = int(input())
#     happyday = []
#     for _ in range(n):
#         happyday.append(int(input())-1)
#     del happyday[0]
#     for i in happyday:
#         happyday=set(happyday)
#         happyday -= set(range(i*2,max(happyday)+1, i))
#         continue
#     print(f"#{t+1} {len(happyday)}")

# 6019
# for t in range(int(input())):
#     d,a,b,f = map(int, input().split())
#     result = (d / (a+b))*f
#     print(f"#{t+1}", "%.10f" %result)

#5215
# def solution(b,a):
#     board = [[0 for _ in range(b+2)]for _ in range(a+2)]
#     for i in range(1,a+1):
#         for j in range(1,b+1):
#             if cal[i-1] > j:
#                 board[i][j] = board[i-1][j]
#             else:
#                 board[i][j] = max(score[i-1]+board[i-1][j-cal[i-1]], board[i-1][j])
#     return board[a][b]

# for t in range(int(input())):
#     n, l = map(int, input().split())
#     hamb = [list(map(int, input().split()))for _ in range(n)]
#     cal = []
#     score = []
#     for i in range(n):
#         score.append(hamb[i][0])
#         cal.append(hamb[i][1])
#     print(f"#{t+1} {solution(l,n)}")

a = input()
b = ' '
cnt = 1
for i in range(len(a)):
    if a[i] == b:
        cnt += 1
if a[0] == ' ':
    cnt -= 1
if a[-1] == ' ':
    cnt -= 1
print(cnt)