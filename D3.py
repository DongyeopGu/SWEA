# 1208 flatten
# for test_case in range(10):
#     N = int(input())
#     dump = list(map(int, input().split()))
#     dump_list = sorted(dump)
#     for i in range(N):
#         a = dump_list[99]
#         b = dump_list[0]
#         a -= 1
#         b += 1
#         dump_list[99] = a
#         dump_list[0] = b
#         dump_list = sorted(dump_list)
        
#     print(f"#{test_case + 1} {dump_list[99] - dump_list[0]}")

# 1209. sum
for test_case in range(10):
    N = int(input())
    num = [list(map(int, input().split())) for i in range(100)]
    num_rot = [[num[i][j] for i in range(100)]for j in range(100)]
    sum_row = []
    sum_col = []
    sum_left = []
    sum_right = []
    for i in range(100):
        sum_col.append(sum(num[i]))
        sum_row.append(sum(num_rot[i]))
        sum_left.append(num[i][i])
        sum_right.append(num_rot[i][i])
    s_l = sum(sum_left)
    s_r = sum(sum_right)
    t_max = max(max(sum_col), max(sum_row), s_l, s_r)
    print(f"#{N} {t_max}")