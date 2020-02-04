<<<<<<< HEAD
# for test_case in range(10):         # 10번의 테스트 케이스 입력
#     N = int(input())                # 가로길이 입력
#     height = list(map(int, input().split()))        # 빌딩 높이 입력
#     sum_view = 0                    # 조망권 합 넣을 변수 선언
#     dif_height = 0                  # 왼쪽 조망권 확보한 곳 찾을 변수
#     dif_height_1 = 0                # 오른쪽 조망권 확보한 곳 찾을 변수
#     for i in range(2, N-2):         # 빌딩 있는 곳 반복
#         if height[i-2] > height[i-1]:       # 왼쪽 두번째, 첫번째 비교 후 큰 값 반환
#             dif_height = height[i-2]
#         else:
#             dif_height = height[i-1]        
#         if height[i+1] > height[i+2]:       # 오른쪽 두번째, 첫번째 비교 후 큰 값 반환
#             dif_height_1 = height[i+1]
#         else:
#             dif_height_1 = height[i+2]
#         if height[i] - dif_height > 0 and height[i] - dif_height_1 > 0:        # 왼쪽과 오른쪽 차이가 양수일 때 중간값 차이를 계속 더함
#             sum_view += (min(height[i] - dif_height, height[i] - dif_height_1))
#     print(f"#{test_case + 1} {sum_view}")
<<<<<<< HEAD

a ='12344312332'
n = ['00']+ [str(i*11)for i in range(1,10)]
for i in range(len(n)):
    if n[i] not in a:
        print('a')
    else:
        a = a.replace(str(n[i]), '')
print(a)
=======
>>>>>>> d9c887f951c8f79e834d9d7f5519014758706bb0
=======
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
>>>>>>> f472ca426ea3cc94f71bb089bedd31522a074162
