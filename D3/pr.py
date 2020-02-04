for test_case in range(int(input())):
    N, K = map(int, input().split())
    a = list(range(1,13))
    n = len(a)
    b = []
    result = 0
    for i in range(1 << n):
        for j in range(n+1):
            if i & (1 << j):
                b.append(a[j])
        if len(b) == N:
            if sum(b) == K:
                result += 1
        b = []
    print(f"#{test_case+1} {result}")