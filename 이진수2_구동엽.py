for t in range(int(input())):
    n = float(input())
    result = ''
    cnt = 0
    while True:
        a = n * 2
        result += str(int(a))
        n = a - int(a)
        cnt += 1
        if n == 0.0:
            break
        if cnt > 13:
            break
    if cnt > 13:
        print(f"#{t+1} overflow")
    else:
        print(f"#{t+1} {result}")