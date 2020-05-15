def sol(a):
    global cnt, result
    if a >= n:
        if result > cnt:
            result = cnt
        return
    if result < cnt:
        return
    b = a
    c = arr[b]

    for i in range(b+c, b, -1):
        cnt += 1
        sol(i)
        cnt -= 1

for t in range(int(input())):
    arr = list(map(int, input().split()))
    n = arr[0]
    result = 987654321
    cnt = 0
    sol(1)
    print(f"#{t+1} {result-1}")