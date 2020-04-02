for t in range(int(input())):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append([c[i], i+1])
    cnt = 0
    while len(a) != 1:
        a[0][0] //= 2
        if a[0][0] == 0:
            if n + cnt < m:
                a.pop(0)
                a.append([c[n+cnt], n+cnt+1])
                cnt += 1
            else:
                a.pop(0)
        else:
            a.append(a.pop(0))
    print(f"#{t+1} {a[0][1]}")