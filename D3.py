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
# for test_case in range(10):
#     N = int(input())
#     num = [list(map(int, input().split())) for i in range(100)]
#     num_rot = [[num[i][j] for i in range(100)]for j in range(100)]
#     sum_row = []
#     sum_col = []
#     sum_left = []
#     sum_right = []
#     for i in range(100):
#         sum_col.append(sum(num[i]))
#         sum_row.append(sum(num_rot[i]))
#         sum_left.append(num[i][i])
#         sum_right.append(num_rot[i][i])
#     s_l = sum(sum_left)
#     s_r = sum(sum_right)
#     t_max = max(max(sum_col), max(sum_row), s_l, s_r)
#     print(f"#{N} {t_max}")

# 1213. String
# for test_case in range(10):
#     T = int(input())
#     find_string = input()
#     string = input()
#     count = 0
#     for i in range(len(string)-len(find_string)+1):
#         if string[i:i+len(find_string)] == find_string:
#             count += 1
#     print(f"#{T} {count}")

# 1215. 회문
# for test_case in range(10):
#     N = int(input())
#     word = [list(map(str, input())) for i in range(8)]
#     word_rot = [[word[i][j]for i in range(8)]for j in range(8)]
#     find_pal = []
#     find_pal_1 = []
#     count = 0
#     for i in range(8):
#         for j in range(9-N):
#             find_pal = list(reversed(word[i][j:j+N]))
#             find_pal_1 = list(reversed(word_rot[i][j:j+N]))
#             if word[i][j:j+N] == find_pal:
#                 count += 1
#             if word_rot[i][j:j+N] == find_pal_1:
#                 count += 1
#     print(f"#{test_case + 1} {count}")

# 1216. 회문2
# for test_case in range(10):
#     T = int(input())
#     word = [list(map(str, input())) for i in range(100)]
#     word_rot = [[word[i][j]for i in range(100)]for j in range(100)]
#     find_pal = []
#     find_pal_1 = []
#     li = []
#     for i in range(100):
#         for j in range(100):
#             for N in range(j, 101):
#                 find_pal = list(reversed(word[i][j:N]))
#                 find_pal_1 = list(reversed(word_rot[i][j:N]))
#                 if word[i][j:N] == find_pal:
#                     li.append(len(find_pal))
#                 if word_rot[i][j:N] == find_pal_1:
#                     li.append(len(find_pal_1))
#     print(f"#{test_case + 1} {max(li)}")

# 1217. 거듭제곱(재귀)
# def involution(a, n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return a
#     else:
#         return a * involution(a, n-1)
        

# for test_case in range(10):
#     N = int(input())
#     a, b = map(int, input().split())
#     print(f"#{N} {involution(a, b)}")

# 1220. Magnetic
# for test_case in range(10):
#     N = int(input())
#     mag = [list(map(int, input().split())) for i in range(N)]
#     mag_rot = [[mag[i][j] for i in range(N)]for j in range(N)]
#     mag_store = []
#     count = 0
#     for i in range(N):
#         mag_store = list(filter(lambda x: x != 0, mag_rot[i]))
#         a = len(mag_store)
#         for j in range(a-1):
#             if mag_store[j:j+2] == [1, 2]:
#                 count += 1
#     print(count)
# 1221. GNS
# for test_case in range(int(input())):
#     T, length = map(str, input().split())
#     num_str = list(map(str, input().split()))
#     a = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
#     b = list(range(10))
#     print(T)
#     for i in range(int(length)):
#         for j in range(10):
#             if a[j] == num_str[i]:
#                 num_str[i] = j 
#     new_str = sorted(num_str)
#     for i in range(int(length)):
#         for j in range(10):
#             if b[j] == new_str[i]:
#                 new_str[i] = a[j]
#     print(' '.join(new_str))

# 1225. 암호생성기
# def pwd_create(a):
#     while True:
#         b = 0
#         for i in range(5):
#             b = a[7]
#             a[7] = a[0] - i
#             a[0], a[1], a[2], a[3], a[4], a[5], a[6] = a[1], a[2], a[3], a[4], a[5], a[6], b
#         if a[0] - 1 < 0 or a[7] == 0:
#             break
#     return a    

for test_case in range(10):
    T = int(input())
    a = list(map(int, input().split()))
    b = list()
    
    for i in range(1, 6):
        a.append(a[0]-i)
        del a[0]
        print(a)
        
        