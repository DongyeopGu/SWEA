# 3142 영준이와 신비한 뿔의 숲
for t in range(int(input())):
    n, m = map(int, input().split())
    x = n - m
    y = 2*m - n
    print(f"#{t+1} {y} {x}")

