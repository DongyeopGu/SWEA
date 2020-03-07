dx = [0,0,-1,1]
dy = [-1,1,0,0]
tunnel_type = {
    1:[[1,3,4,5],[1,3,6,7],[1,2,5,6],[1,2,4,7]],
    2:[[],[],[1,2,5,6],[1,2,4,7]],
    3:[[1,3,4,5],[1,3,6,7],[],[]],
    4:[[],[1,3,6,7],[1,2,5,6],[]],
    5:[[],[1,3,6,7],[],[1,2,4,7]],
    6:[[1,3,4,5],[],[],[1,2,4,7]],
    7:[[1,3,4,5],[],[1,2,5,6],[]]
    }

for t in range(int(input())):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split()))for _ in range(n)]
    cnt = 1
    start = [(r,c)]
    time = 1
    while True:
        if time == l:
            break
        for i in range(len(start)):
            a = start.pop(0)
            for j in range(4):
                if tunnel_type[tunnel[a[0]][a[1]]][j]:
                    if 0 <= a[0]+dx[j] < n and 0 <= a[1]+dy[j] < m and tunnel[a[0]+dx[j]][a[1]+dy[j]] != 0:
                        if tunnel[a[0]+dx[j]][a[1]+dy[j]] in tunnel_type[tunnel[a[0]][a[1]]][j]:
                            if (a[0]+dx[j],a[1]+dy[j]) not in start:
                                start.append((a[0]+dx[j],a[1]+dy[j]))
                                cnt += 1
            tunnel[a[0]][a[1]] = 0
        time += 1
    print(f"#{t+1} {cnt}")