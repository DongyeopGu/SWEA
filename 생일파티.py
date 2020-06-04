for t in range(int(input())):
    n, m =  map(int, input().split())
    a = [[]for _ in range(n+1)]
    for i in range(m):
        n1, n2 = map(int,input().split())
        a[n1].append(n2)
        a[n2].append(n1)
    result = set()
    result.update(a[1])
    for i in a[1]:
        result.update(a[i])
    if 1 in result:
        result.remove(1)
    print(f"#{t+1} {len(result)}")