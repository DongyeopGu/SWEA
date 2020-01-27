# T = int(input())  # 테스트 케이스
# for i in range(T):    # 테스트 케이스 반복
#     N = int(input())  # 테스트 1<= N <= 10
#     pascal_1 = [1]
#     pascal_2 = [1, 1]
#     pascal_ = [1, 1]
#     if N == 1:
#         print(''.join(map(str, pascal_1)))
#     elif N == 2:
#         print(''.join(map(str, pascal_1)))
#         print(' '.join(map(str, pascal_2)))
#     else:
#         print(''.join(map(str, pascal_1)))
#         print(' '.join(map(str, pascal_2)))
#         pascal_n = [1] * N
#         for k in range(1, N-1):
#             pascal_n = pascal_    
#             pascal_n[k] = pascal_[k] + pascal_[k-1]
#             print(k, pascal_n)


# for T in range(int(input())):
#     N,K=map(int,input().split())
#     M=[list(map(int,input().split())) for i in range(N)]
#     M+=[[M[i][j]for i in range(N)]for j in range(N)]
#     c=0
#     for i in range(2*N):
#         for j in range(N-K+1):
#             if sum(M[i][j:j+K])==K and (j==0 or (j>0 and not M[i][j-1])) and (j+K==N or (j+K<N and not M[i][j+K])):
#                 c+=1
#     print("#%d %d"%(T+1,c))
for i in range(int(input())):
    sudoku = [list(map(int, input().split())) for i in range(9)]
    sudoku_1 = list([sudoku[i][j] for i in range(9)] for j in range(9))
    result = 0
    
    sudoku_2 = []
    for j in range(3):
        for m in range(3):
            sudoku_2 += [sudoku[j][m]]
    for k in range(3):
        for l in range(3,6):
            sudoku_2 += [sudoku[k][l]]
    for k in range(3):
        for l in range(6,9):
            sudoku_2 += [sudoku[k][l]]
    
    for j in range(3,6):
        for m in range(3):
            sudoku_2 += [sudoku[j][m]]
    for k in range(3,6):
        for l in range(3,6):
            sudoku_2 += [sudoku[k][l]]
    for k in range(3,6):
        for l in range(6,9):
            sudoku_2 += [sudoku[k][l]]

    for j in range(6,9):
        for m in range(3):
            sudoku_2 += [sudoku[j][m]]
    for k in range(6,9):
        for l in range(3,6):
            sudoku_2 += [sudoku[k][l]]
    for k in range(6,9):
        for l in range(6,9):
            sudoku_2 += [sudoku[k][l]]

    for i in range(0,81,9):
        print(set(sudoku_2[i:i+9]))
    for j in range(9):
        print(len(set(sudoku_1[j])))
    