# 3142 영준이와 신비한 뿔의 숲
# for t in range(int(input())):
#     n, m = map(int, input().split())
#     x = n - m
#     y = 2*m - n
#     print(f"#{t+1} {y} {x}")

# 3233 정삼각형 분할
# for t in range(int(input())):
#     n, m = map(int, input().split())
#     a = n**2//m**2
#     print(f"#{t+1} {a}")
a= 6
b= 5
for i in range(a-1,-1,-1):
    for j in range(b+1,10):
        if i + j == a + b:
            if j > 7:
                break
            print(i,j)