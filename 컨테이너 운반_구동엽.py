for t in range(int(input())):
    n,m = map(int, input().split())
    weight = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    result = 0
    for i in range(m):
        a = 0
        for j in weight:
            if truck[i] >= j >= a:
                a = j
        if a != 0:
            weight.remove(a)
        result += a
    print(f"#{t+1} {result}")
    