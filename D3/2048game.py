def left(a,i=0):              #왼쪽 붙이기
    b = []
    for j in range(len(a[i])-1):
        if a[i][j] != a[i][j+1]:
            b.append(a[i][j])
            if j == len(a[i])-2:
                b.append(a[i][j+1])
        if a[i][j] == a[i][j+1] and a[i][j] != 0:
            b.append(2*a[i][j])
            a[i][j+1] = 0
    for j in range(1, len(b)):
        if b[j] == 0:
            del b[j]
            b.append(0)
    if b[0] == 0:
        del b[0]
        b.append(0)
    c = n - len(b)
    for j in range(c):
        b.append(0)
    return b


for t in range(int(input())):
    n, case = map(str, input().split())
    n = int(n)
    a = [list(map(int, input().split()))for _ in range(n)]
    print(f"#{t+1}")
    if case == "left":
        for i in range(n):
            print(' '.join(map(str, left(a,i))))
  