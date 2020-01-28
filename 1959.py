# 1959. 두 개의 숫자열
# for test_case in range(int(input())):
#     N, M = map(int, input().split())
#     A = list(map(int, input().split()))
#     B = list(map(int, input().split()))
#     if N > M:
#         C = []
#         result = list(range(N-M+1))
#         for k in range(N-M+1):
#             for i in range(M):
#                 C.append(A[i+k] * B[i])
#         for j in range(N-M+1):
#             result[j] = sum(C[j*M:(j*M)+M])
        
#     elif M > N:
#         D = []
#         result = list(range(M-N+1))
#         for k in range(M-N+1):
#             for i in range(N):
#                 D.append(A[i] * B[i+k])
#         for j in range(M-N+1):
#             result[j] = sum(D[j*N:(j*N)+N])
#     print(f"#{test_case+1} {max(result)}")

# 1948. 날짜 계산기
# for test_case in range(int(input())):
#     m_1, d_1, m_2, d_2 = map(int, input().split())
#     d_3 = (m_2 - m_1) * 30 + (d_2 - d_1) + 1
#     m_list_31 = [1, 3, 5, 7, 8, 10, 12]
#     m_list_30 = [4, 6, 9, 11]
#     m_list_28 = [2]
#     m_3 = list(range(m_1, m_2))
#     for i in range(len(m_3)):
#         if m_3[i] in m_list_31:
#             d_3 += 1
#         elif m_3[i] in m_list_28:
#             d_3 = d_3 - 2
#     print(f"#{test_case+1} {d_3}")

# 1946. 간단한 압축풀기
# for test_case in range(int(input())):
#     l = []
#     a = []
#     count = 0
#     for n in range(int(input())):
#         l += [list(map(str, input().split()))]
#     print(f"#{test_case + 1}")
#     for i in range(len(l)):
#         for j in range(int(l[i][1])):
#             a.append(l[i][0])
#     for k in range(0,len(a),10):
#         print(''.join(a[k:k+10]))

# 1945. 간단한 소인수분해
# for test_case in range(int(input())):
#     N = int(input())
#     a = 0
#     b = 0
#     c = 0
#     d = 0
#     e = 0
#     for i in range(N):
#         if N % 2 == 0:
#             a += 1
#             N = N / 2
#         elif N % 3 == 0:
#             b += 1
#             N = N / 3
#         elif N % 5 == 0:
#             c += 1
#             N = N / 5
#         elif N % 7 == 0:
#             d += 1
#             N = N / 7
#         elif N % 11 == 0:
#             e += 1
#             N = N / 11
#      print(f"#{test_case +1} {a} {b} {c} {d} {e}")

# 1204. 최빈수 구하기
# for test_case in range(int(input())):
#     N = int(input())
#     a = list(map(int, input().split()))
#     b = dict()
#     sorted_a = sorted(a)
#     for i in sorted_a:
#         b[i] = sorted_a.count(i)
#     c = max(b.values())
#     score = 0
#     for j, k in b.items():
#         if k == c:
#             score = j
#     print(f"#{test_case +1} {score}")

# 1284. 수도 요금 경쟁
# for test_case in range(int(input())):
#     P, Q, R, S, W = map(int, input().split())
#     A_price = P * W
#     if W <= R:
#         B_price = Q
#     else:
#         B_price = Q + (W - R) * S
#     if A_price < B_price:
#         print(f"#{test_case + 1} {A_price}")
#     else:
#         print(f"#{test_case + 1} {B_price}")

# 1285. 돌 던지기
# for test_case in range(int(input())):
#     N = int(input())
#     dist = list(map(int, input().split()))
#     abs_dist = list(range(N))
#     for i in range(N):
#         abs_dist[i] = abs(dist[i])
#     print(f"#{test_case + 1} {min(abs_dist)} {abs_dist.count(min(abs_dist))}")

# 1288. 새로운 불면증
# for test_case in range(int(input())):
#     N = input()
#     a = list(map(int, N))
#     c = list()
#     result = 0
#     for i in range(1, 10**6):
#         c += list(map(int, str(int(N) * i)))
#         if len(set(c)) == 10:
#             result = int(N) * i
#             break
#     print(f"#{test_case + 1} {result}")

# 1928. base64 decoder

# 1961. 숫자 회전
# def rotate(m, d):
#     N = len(m)
#     a = [[0] * N for i in range(N)]

#     if d % 4 == 1:
#         for r in range(N):
#             for c in range(N):
#                 a[c][N-1-r] = m[r][c]
#     elif d % 4 == 2:
#         for r in range(N):
#             for c in range(N):
#                 a[N-1-r][N-1-c] = m[r][c]
#     elif d % 4 == 3:
#         for r in range(N):
#             for c in range(N):
#                 a[N-1-c][r] = m[r][c]
#     else:
#         for r in range(N):
#             for c in range(N):
#                 a[r][c] = m[r][c]

#     return a

# for test_case in range(int(input())):
#     N = int(input())
#     num = [list(map(int, input().split())) for i in range(N)]
#     a = rotate(num, 1)
#     b = rotate(num, 2)
#     c = rotate(num, 3)
#     print(f"#{test_case + 1}")
#     for i in range(N):
#         print(''.join(map(str, a[i])), ''.join(map(str, b[i])), ''.join(map(str, c[i])))

# 1954. 달팽이 숫자
# for test_case in range(int(input())):
#     N = int(input())
#     snail = [[0 for i in range(N)] for j in range(N)]
#     row = N
#     col = N
#     count = 0
#     offset = 0
#     while row > 0 and col > 0:
#         for i in range(offset, offset+col):
#             count += 1
#             snail[offset][i] = count
#         for i in range(offset+1, offset+row):
#             count += 1
#             snail[i][offset+col-1] = count
#         for i in range(offset+col-2, offset-1, -1):
#             count += 1
#             snail[offset+row-1][i] = count
#         for i in range(offset+row-2, offset, -1):
#             count += 1
#             snail[i][offset] = count
#         offset += 1
#         row -= 2
#         col -= 2
#     print(f"#{test_case + 1}")
#     for i in range(N):
#         print(' '.join(map(str, snail[i])))
