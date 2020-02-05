for t in range(int(input())):
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    n = len(a)
    b = []
    result = 0
    cnt = 0
    for i in range(1 << n):
        for j in range(n+1):
            if i & (1 << j):
                result += a[j]
                if result>K:
                    continue
        if result == K:
            cnt += 1
        result=0

    print(f"#{t+1} {cnt}")