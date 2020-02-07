n = int(input())    #스위치개수
switch = list(map(int, input().split()))
m = int(input())    #사람수
cnt = 0
a = 0
for _ in range(m):
    student = list(map(int, input().split()))
    if student[0] == 1:
        k = student[1] - 1
        for b in range(k,n,k+1):
            switch[b] = 1 - switch[b]
    else:
        j = student[1] - 1
        switch[j] = 1 - switch[j]
        for i in range(1,j+1):
            if switch[j-i] != switch[j+i]:
                break
            if switch[j-i] == switch[j+i]:
                switch[j-i] = 1 - switch[j-i]
                switch[j+i] = 1 - switch[j+i]
                continue
            
for i, e in enumerate(switch):
    if i and not (i%20):
        print()
    print(e, end=' ')