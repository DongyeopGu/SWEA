# 1959. 두 개의 숫자열
for test_case in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if N > M:
        C = []
        result = list(range(N-M+1))
        for k in range(N-M+1):
            for i in range(M):
                C.append(A[i+k] * B[i])
        for j in range(N-M+1):
            result[j] = sum(C[j*M:(j*M)+M])
        
    elif M > N:
        D = []
        result = list(range(M-N+1))
        for k in range(M-N+1):
            for i in range(N):
                D.append(A[i] * B[i+k])
        for j in range(M-N+1):
            result[j] = sum(D[j*N:(j*N)+N])
    print(f"#{test_case+1} {max(result)}")
            
        
    

