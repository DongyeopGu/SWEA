def pipe(a,n):
    cnt = 0
    a[0][0] = 1
    a[0][1] = 1
    for i in range(n):
        for j in range(1,n):
            a[i][1+j] = 1
            if i+j > n-1:
                break
            if i >n-1:
                break
            


N = int(input())
pipemap = [list(map(int, input().split()))for _ in range(N)]
print(pipe(pipemap,N))