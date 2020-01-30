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
