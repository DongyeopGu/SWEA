for test_case in range(int(input())):
    N, A, B = map(int, input().split())
    a = []
    for R in range(1, int(N**0.5)+1):
        for C in range(1 ,int(N/R)+1):
            a.append(A*abs(R-C) + B*(N-R*C))
    print(f"#{test_case+1} {min(a)}")