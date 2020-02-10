def rotation(a):
    for i in range(n):
        for j in range(i):
            a[i][j], a[j][i] = a[j][i], a[i][j]
    return a
def rev(a):
    for i in range(n):
        a[i] = a[i][::-1]
    return a
def left(a):             
    for i in range(n):
        for j in range(a[i].count(0)):
            a[i].append(a[i].pop(a[i].index(0)))
        for j in range(1,n):
            if a[i][j-1] == a[i][j]:
                a[i][j-1] = a[i][j-1]*2
                a[i][j] = 0
        for j in range(a[i].count(0)):
            a[i].append(a[i].pop(a[i].index(0)))
    return a

def right(a):
    rev(a)
    left(a)
    return rev(a)
def up(a):
    rotation(a)
    left(a)
    return rotation(a)
def down(a):
    rotation(a)
    right(a)
    return rotation(a)

for t in range(int(input())):
    n, case = map(str, input().split())
    n = int(n)
    a = [list(map(int, input().split()))for _ in range(n)]
    print(f"#{t+1}")
    if case == "left":
        a = left(a)
        for i in range(n):
            print(' '.join(map(str, a[i])))
    if case == "right":
        a = right(a)
        for i in range(n):
            print(' '.join(map(str, a[i])))
    if case == "up":
        a = up(a)
        for i in range(n):
            print(' '.join(map(str, a[i])))
    if case == "down":
        a = down(a)
        for i in range(n):
            print(' '.join(map(str, a[i])))       
    