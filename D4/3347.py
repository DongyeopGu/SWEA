for t in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = [0] * n
    for i in range(m):
        for j in range(n):
            if a[j]<=b[i]:
                c[j] += 1
                break
    print(f"#{t+1} {c.index(max(c))+1}")