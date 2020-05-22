def dis():
    key = [float('inf')for _ in range(n+1)]
    visit = [0 for _ in range(n+1)]
    check = set()
    check.add(0)
    key[0] = 0
    while True:
        min_key = float('inf')
        s = -1
        for i in check:
            if key[i] < min_key:
                min_key = key[i]
                s = i
        visit[s] = 1
        check.remove(s)
        if s == n:
            return key[s]
        for e, w in l[s]:
            if key[e] > key[s] + w and not visit[e]:
                key[e] = key[s] + w
                check.add(e)

for t in range(int(input())):
    n, e = map(int, input().split())
    l = {}
    for _ in range(e):
        s, e, w = map(int, input().split())
        if s not in l:
            l[s] = [(e, w)]
        else:
            l[s] += [(e, w)]
    result = dis()
    print(f"#{t+1} {result}")