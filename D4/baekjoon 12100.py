import copy

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
def my_max(a):
    max_v = 0
    for i in range(n):
        for j in range(n):
            if a[i][j] > max_v:
                max_v = a[i][j]
    return max_v

def solv(cnt, a):
    global result
    if cnt == 5:
        result = max(result, my_max(a))
    if cnt<5:
        copy_a = copy.deepcopy(a)
        up(copy_a)
        solv(cnt+1, copy_a)
        
        copy_a = copy.deepcopy(a)
        down(copy_a)
        solv(cnt+1, copy_a)

        copy_a = copy.deepcopy(a)
        left(copy_a)
        solv(cnt+1, copy_a)
        
        copy_a = copy.deepcopy(a)
        right(copy_a)
        solv(cnt+1, copy_a)

n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
result = 0
solv(0,a)
print(result)