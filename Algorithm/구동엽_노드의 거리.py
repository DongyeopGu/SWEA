def solv(z):
    global result
    q.append(z)
    visit[z] = 1
    while q:
        c = q.pop(0)
        for i in range(1,v+1):
            if a[c][i] == 1 and visit[i]==0:
                q.append(i)
                visit[i] = 1
                d[i] = d[c] + 1
                if i == end:
                    result = d[i]
                    return

for t in range(int(input())):
    v, e = map(int, input().split())
    a = [[0 for _ in range(v+1)]for _ in range(v+1)]
    visit = [0] * (v+1)
    d = [0] * (v+1)
    for i in range(e):
        x, y = map(int,input().split())
        a[x][y] = 1
        a[y][x] = 1
    start, end = map(int, input().split())

    q=[]
    result = 0
    solv(start)
    
    print(f"#{t+1} {result}")