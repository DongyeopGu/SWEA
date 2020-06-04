def sol(n):
    q = [n]
    cnt =0
    while q:
        cnt += 1
        a = q.pop()
        for i in v_1[a]:
            q.append(i)
    return cnt

for t in range(int(input())):
    v, e, n1, n2 = map(int, input().split())
    n3 = 987654321
    v_1 = [[]for _ in range(v+1)]
    v_2 = [[]for _ in range(v+1)]
    data = [*map(int, input().split())]
    for i in range(e):
        v_1[data[2*i]].append(data[2*i+1])
        v_2[data[2*i+1]].append(data[2*i])

    while n1 != n3:
        n1 = v_2[n1][0]
        n3 = n2
        while n3>1 and n1 != n3:
            n3=v_2[n3][0]
    result = sol(n1)
    print(f"#{t+1} {n1} {result}")