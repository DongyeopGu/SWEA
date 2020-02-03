for test_case in range(int(input())):
    N, A, B = map(int, input().split())
    a = []
    for R in range(1, N):
        for C in range(1, N):
            if R * C <= N:
                if A*abs(R-C) + B*(N-R*C) >= 0:
                    a.append(A*abs(R-C) + B*(N-R*C))
    print(f"#{test_case} {min(a)}")
