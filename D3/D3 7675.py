for t in range(int(input())):
    n = int(input())
    arr = [0]*n
    cnt = 0
    a = list(input().split())
    for i in a:
        flag = 0
        for j in i:
            if not flag and j.isupper():
                flag = 1
            elif j.isdigit() or (flag and j.isupper()):
                flag = 0
                break
        if flag:
            arr[cnt] += 1
        if ('.' in i) or ('!' in i) or ('?' in i):
            cnt += 1
    print(f"#{t+1} {' '.join(map(str, arr))}")