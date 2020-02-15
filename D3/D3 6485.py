for t in range(int(input())):
    arr = [0]*5001
    for i in range(int(input())):
        a , b = map(int, input().split())
        for j in range(a,b+1):
            arr[j] += 1
    p = int(input())
    arr_1 = [0]*p
    for i in range(p):
        c = int(input())
        arr_1[i] = arr[c]
    print(f"#{t+1} {' '.join(map(str, arr_1))}")