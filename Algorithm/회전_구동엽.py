for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(m):
        b = a.pop(0)
        a.append(b)
    print(f"#{t+1} {a[0]}")