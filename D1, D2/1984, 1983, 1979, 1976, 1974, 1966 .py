# # 중간 평균값 구하기
# T = int(input())
# for test_case in range(T):
#     N = list(map(int, input().split()))
#     max_num = N[0]
#     min_num = N[0]
#     for i in range(len(N)):
#         if min_num > N[i]:
#             min_num = N[i]
    
#         if N[i] > max_num:
#             max_num = N[i]
#     N.remove(min_num)
#     N.remove(max_num)
#     result = round((sum(N) / len(N)))
    
#     print(f"#{test_case+1} {result}")

# #  1983 조교의 성적 매기기
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     score = []
#     grade_score = dict()
#     total_score = list(range(N))
#     for n in range(N):
#         score_input = list(map(int, input().split(' ')))
#         score.append(score_input)
#     for i in range(N):
#         total_score[i] = score[i][0] * 0.35 + score[i][1] * 0.45 + score[i][2] * 0.2
#     sorted_score = sorted(total_score, reverse=True)
#     count = 0
#     grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
#     for j in range(N):
#         if count <= N/10:
#             grade_score[sorted_score[j]] = grade[int(j/(N/10))] 
#             count += 1
#             count = 0
#     print(f"#{test_case + 1} {grade_score[total_score[K-1]]}")

# # 1979 어디에 단어가 들어갈 수
# T = int(input())
# for test_case in range(T):
#     N, K = map(int, input().split())
#     mapping = []
#     result = 0
#     for n in range(N):
#         map_set = list(map(int, input().split()))
#         mapping.append(map_set)
#     mapping += ([[mapping[i][j]for i in range(N)]for j in range(N)])
    
#     for i in range(N * 2):
#         for j in range(N-K+1):
#             if sum(mapping[i][j:j+K]) == K and (j==0 or (j>0 and not mapping[i][j-1])) and (j+K==N or (j+K<N and not mapping[i][j+K])):
#                 result += 1
#     print(f"#{test_case + 1} {result}")

# # 1976. 시각덧셈
# for i in range(int(input())):
#     h_1, m_1, h_2, m_2 = map(int, input().split())
#     h = h_1 + h_2
#     m = m_1 + m_2
#     if m > 59:
#         m = m -60
#         h = h+1
#     if h > 12:
#         h = h - 12
#     print(f"#{i+1} {h} {m}")

# 1974. 스도쿠
# for test_case in range(int(input())):
#     sudoku = [list(map(int, input().split())) for i in range(9)]
#     sudoku_1 = list([sudoku[i][j] for i in range(9)] for j in range(9))
#     result = 0
#     sudoku_2 = []
#     for j in range(3):
#         for m in range(3):
#             sudoku_2 += [sudoku[j][m]]
#     for k in range(3):
#         for l in range(3,6):
#             sudoku_2 += [sudoku[k][l]]
#     for k in range(3):
#         for l in range(6,9):
#             sudoku_2 += [sudoku[k][l]]
    
#     for j in range(3,6):
#         for m in range(3):
#             sudoku_2 += [sudoku[j][m]]
#     for k in range(3,6):
#         for l in range(3,6):
#             sudoku_2 += [sudoku[k][l]]
#     for k in range(3,6):
#         for l in range(6,9):
#             sudoku_2 += [sudoku[k][l]]

#     for j in range(6,9):
#         for m in range(3):
#             sudoku_2 += [sudoku[j][m]]
#     for k in range(6,9):
#         for l in range(3,6):
#             sudoku_2 += [sudoku[k][l]]
#     for k in range(6,9):
#         for l in range(6,9):
#             sudoku_2 += [sudoku[k][l]]

#     for i in range(0,81,9):
#         if len(set(sudoku_2[i:i+9])) != 9:
#             result = 0
#             break
#         else:
    
#             for j in range(9):
#                 if len(set(sudoku[j])) != 9 or len(set(sudoku_1[j])) != 9:
#                     result = 0
#                     break
#                 else:
#                     result = 1
#     print(f"#{test_case+1} {result}")

# 1970. 쉬운 거스름돈
# for test_case in range(int(input())):
#     N = int(input())
#     money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
#     print(f'#{test_case + 1}')
#     for money in money_list:
#         value = N // money
#         N = N % money
#         print(value, end=' ')
#     print()
    
# 1966. 숫자 정렬
# for test_case in range(int(input())):
#     N = int(input())
#     num_list = list(map(int, input().split(' ')))
#     _list = 0
#     for i in range(N):
#         for j in range(N-i-1):
#             if num_list[j] > num_list[j+1]:
#                 _list = num_list[j]
#                 num_list[j] = num_list[j+1]
#                 num_list[j+1] = _list
#     a = list(map(str, num_list))
#     print(f"#{test_case + 1} {' '.join(a)}")
