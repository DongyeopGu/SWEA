# 3314
# for t in range(int(input())):
#     score = list(map(int, input().split()))
#     for i in range(len(score)):
#         if score[i] < 40:
#             score[i] = 40
#     print(f"#{t+1} {sum(score)//5}")
# 3376 파도반 수열
# def wave(n):
#     a = [1,1,1]
#     b = [1] * n
#     if n <=3:
#         return 1
#     else:
#         for i in range(3,n):
#             b[i] = b[i-2] + b[i-3]
#     return b[n-1]
# for t in range(int(input())):
#     N = int(input())
#     print(f"#{t+1} {wave(N)}")

# 3408 세가지합

# for t in range(int(input())):
#     N = int(input())
#     sum_1 = N*(N+1)//2
#     sum_2 = N*(N*2)//2
#     sum_3 = N*(N*2+2)//2
#     print(f"#{t+1} {sum_1} {sum_2} {sum_3}")

# 3431. 준환이의 운동관리
for t in range(int(input())):
    L, U, X = map(int, input().split())
    if U < X:
        print(f"#{t+1} {-1}")
    elif L <= X <= U:
        print(f"#{t+1} {0}")
    else:
        print(f"#{t+1} {L-X}")