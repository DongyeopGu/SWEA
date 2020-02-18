def check(a):
    h = a[0]
    i = 1
    count 
    while i < n:
        if h == a[i]:
            i += 1
            continue
        if h - a[i] == 1:
            if l

n, l = map(int, input().split())
a = [list(map(int, input().split()))for _ in range(n)]
a += [[a[i][j]for i in range(n)] for j in range(n)]
cnt = 0
for i in range(2*n):
    cnt += check(a[i])
print(cnt)
            
            
