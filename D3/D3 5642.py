for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    max_ = -10000
    sum_ = 0
    for i in range(n):
        sum_ += a[i]
        if sum_ > max_:
            max_ = sum_
        if sum_ < 0:
            sum_ = 0
    print(f"#{t+1} {max_}")
