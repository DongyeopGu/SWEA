for t in range(int(input())):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    min_ = 10000*20
    for i in range(1<<n):
        sum_ = 0
        for j in range(n):
            if i &(1<<j):
                sum_ += height[j]
        if sum_ >= b and sum_ < min_:
            min_ = sum_
    print(f"#{t+1} {min_-b}")