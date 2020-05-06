def sol(a,b,c):
    if b == n-1:
        c += arr[a][0]
        result.append(c)
    else:
        for i in range(1,n):
            if not visit[i]:
                c += arr[a][i]
                visit[i]=1
                sol(i,b+1,c)
                visit[i]=0
                c -= arr[a][i]
    

for t in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split()))for _ in range(n)]
    visit = [0]*n
    result = []
    sol(0,0,0)
    print(f"#{t+1} {min(result)}")