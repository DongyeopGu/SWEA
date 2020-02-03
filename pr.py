# # 1491. 원재의 벽
# for test_case in range(int(input())):
#     N, A, B = map(int, input().split())
#     a = []
#     for R in range(1, int(N**0.5)+1):
#         for C in range(1 ,int(N/R)+1):
#             a.append(A*abs(R-C) + B*(N-R*C))
#     print(f"#{test_case+1} {min(a)}")

# 1493. 수의 새로운 연산
for test_case in range(int(input())):
    p, q = map(int, input().split())
    a = []
    dif_p = 0
    dif_q = 0
    for i in range(2,10002):
        a.append(int((i * (i - 1))/2))
    for i in range(1, 10000): # y값 구하기
        if a[i-1] < p < a[i]:
            dif_p = a[i] - p
            p_y = dif_p + 1
            p_x = i + 1 - dif_p
        if a[i-1] == p:
            p_y = 1
            p_x = i
    for i in range(1, 10000): # y값 구하기
        if a[i-1] < q < a[i]:
            dif_q = a[i] - q
            q_y = dif_q + 1
            q_x = i + 1 - dif_q
        if a[i-1] == q:
            q_y = 1
            q_x = i
    sum_pq_x = p_x + q_x
    sum_pq_y = p_y + q_y
    result = (sum_pq_y**2 - sum_pq_y + 2)/2
    

    print(f"#{test_case + 1} {a[sum_pq_x+1] - (sum_pq_y - 1)}")