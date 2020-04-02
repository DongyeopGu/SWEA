for test_case in range(10):
    T = int(input())
    a = list(map(int, input().split()))
    while True:
        b = 0
        for i in range(1, 6):
            b = a[0] - i
            if b <= 0:
                b = 0
                continue
            for j in range(7):
                a[j] = a[j + 1]
            a[7] = b
        if b == 0:
            for j in range(7):
                a[j] = a[j + 1]
            break
    a[7] = 0
    print(f"#{T} {' '.join(list(map(str, a)))}")