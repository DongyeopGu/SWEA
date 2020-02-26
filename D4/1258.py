for t in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                continue
            c = i
            while c < n and a[c][j]:
                r = j
                while r < n and a[c][r]:
                    a[c][r] = 0
                    r += 1
                c += 1
            result.append([c-i, r-j])
    result.sort(key=lambda x : (x[0]*x[1], x[0]))
    print(f"#{t+1} {len(result)}", end=' ')
    for i,j in result:
        print(i,j,end=' ')
    print()    