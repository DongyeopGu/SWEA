dt = [(-1,0), (0,1), (1,0), (0,-1)]
def sol(x,y,num,cnt=0):
    global result
    if cnt == 6:
        result.add(num)
        return
    for delta in dt:
        dx, dy = x + delta[0], y + delta[1]
        if not (0 <= dx < 4 and 0 <= dy < 4):
            continue
        sol(dx,dy,num+a[dx][dy], cnt+1)           
        
for t in range(int(input())):
    a = [list(map(str, input().split()))for _ in range(4)]
    result = set()
    for i in range(4):
        for j in range(4):
            sol(i,j,a[i][j])
    print(f"#{t+1} {len(result)}")
   