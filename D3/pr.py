<<<<<<< HEAD
=======
# 4615. 오셀로
def line(a,b,c):            
    find = False
    for i in range(b+1,N):
        if othello[a][i] == 0:
            break
        elif othello[a][i] == c:
            find = True
            break
    if find:
        for i in range(b+1,N):
            if othello[a][i] != c:
                othello[a][i] = c
                continue
            elif othello[a][i] == c or othello[a][i] == 0:
                break
    find = False
    for i in range(b-1,-1,-1):
        if othello[a][i] == 0:
            break
        elif othello[a][i] == c:
            find = True
            break
    if find:
        for i in range(b-1,-1,-1):
            if othello[a][i] != c:
                othello[a][i] = c
                continue
            elif othello[a][i] == c or othello[a][i] == 0:
                break
    return othello

def sero(a,b,c):
    find = False
    for i in range(a+2,N):
        if othello[i][b] == 0:
            break
        elif othello[i][b] == c:
            find = True
            break
    if find:
        for i in range(a+1,N):
            if othello[i][b] != c:
                othello[i][b] = c
                continue
            if othello[i][b] == c or othello[i][b] == 0:
                break
    find = False
    for i in range(a-2,-1,-1):
        if othello[i][b] == 0:
            break
        elif othello[i][b] == c:
            find = True
            break
    if find:
        for i in range(a-1,-1,-1):
            if othello[i][b] != c:
                othello[i][b] = c
                continue
            if othello[i][b] == c or othello[i][b] == 0:
                break
    return othello

def diag_1(a,b,c):
    find = False
    for i in range(a+2,N):
        for j in range(b+2,N):
            if i - j == a - b:
                if othello[i][j] == 0:
                    break
                elif othello[i][j] == c:
                    find = True
                    break
    if find:
        for i in range(a+1,N):
            for j in range(b+1,N):
                if i - j == a - b:
                    if othello[i][j] != c:
                        othello[i][j] = c
                        continue
                    if othello[i][j] == c or othello[i][j] == 0:
                        break
                    
    find = False
    for i in range(a-2,-1,-1):
        for j in range(b-2,-1,-1):
            if i - j == a - b:
                if othello[i][j] == 0:
                    break
                elif othello[i][j] == c:
                    find = True
                    break
    if find:
        for i in range(a-1,-1,-1):
            for j in range(b-1,-1,-1):
                if i - j == a - b:
                    if othello[i][j] != c:
                        othello[i][j] = c
                        continue
                    if othello[i][j] == c or othello[i][j] == 0:
                        break
    return othello

def diag_2(a,b,c):
    find = False
    for i in range(a+2,N):
        for j in range(b-2,-1,-1):
            if i - j == a - b:
                if othello[i][j] == 0:
                    break
                elif othello[i][j] == c:
                    find = True
                    break
    if find:
        for i in range(a+1,N):
            for j in range(b-1,-1,-1):
                if i - j == a - b:
                    if othello[i][j] != c:
                        othello[i][j] = c
                        continue
                    if othello[i][j] == c or othello[i][j] == 0:
                        break
                        
    find = False
    for i in range(a-2,-1,-1):
        for j in range(b+2,N):
            if i - j == a - b:
                if othello[i][j] == 0:
                    break
                elif othello[i][j] == c:
                    find = True
                    break
    if find:
        for i in range(a-1,-1,-1):
            for j in range(b+1,N):
                if i - j == a - b:
                    if othello[i][j] != c:
                        othello[i][j] = c 
                    elif othello[i][j] == c or othello[i][j] == 0:
                        break
    return othello


for t in range(int(input())):
    N, M = map(int, input().split())
    othello= [[0 for _ in range(N)]for _ in range(N)]
    othello[N//2-1][N//2-1:N//2+1] = [2, 1]
    othello[N//2][N//2-1:N//2+1] = [1, 2]
    for i in range(M):
        put = list(map(int, input().split()))
        othello[put[1]-1][put[0]-1] = put[2]
        line(put[1]-1,put[0]-1,put[2])
        sero(put[1]-1,put[0]-1,put[2])
        diag_1(put[1]-1,put[0]-1,put[2])
        diag_2(put[1]-1,put[0]-1,put[2])
    cnt = [0,0]
    for i in range(N):
        for j in range(N):
            if othello[i][j] == 1:
                cnt[0] += 1
            if othello[i][j] == 2:
                cnt[1] += 1
    print(f"#{t+1} {' '.join(map(str, cnt))}")
        
>>>>>>> 04591ca53f00f6f42490c6fc6ad064b2bb020870
