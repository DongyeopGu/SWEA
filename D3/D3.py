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

# for test_case in range(10):
#     T = int(input())
#     a = list(map(int, input().split()))
#     while True:
#         b = 0
#         for i in range(1, 6):
#             b = a[0] - i
#             if b <= 0:
#                 b = 0
#                 continue
#             for j in range(7):
#                 a[j] = a[j + 1]
#             a[7] = b
#             print(a)
#         if b == 0:
#             for j in range(7):
#                 a[j] = a[j + 1]
#             break
#     a[7] = 0
#     print(f"#{T} {' '.join(list(map(str, a)))}")

# 1228. 암호문 1
# for test_case in range(10):
#     N = int(input())
#     origin_pwd = list(map(int, input().split()))
#     N_1 = int(input())
#     f_command = list(map(str, input().split()))
#     r_command = [[]for i in range(N_1)]
#     I = []
#     for i in range(len(f_command)):
#         if f_command[i].isdigit() == True:
#             f_command[i] = int(f_command[i])
#         else:
#             I.append(i)
#     I.append(len(f_command))
#     for i in range(N_1):
#         for j in range(i+1):
#             r_command[i] = f_command[I[j]:I[j+1]]
#     print(r_command)
#     for i in range(N_1):
#         for j in range(len(r_command[i][3:])):
#             origin_pwd.insert(r_command[i][1]+j, r_command[i][3+j])
#     print(f"#{test_case + 1} {' '.join(map(str , origin_pwd[:10]))}")

# 1229. 암호문2

# for test_case in range(10):
#     N = int(input())
#     origin_pwd = list(map(int, input().split()))
#     N_1 = int(input())
#     f_command = list(map(str, input().split()))
#     r_command = [[]for i in range(N_1)]
#     I = []
#     for i in range(len(f_command)):
#         if f_command[i].isdigit() == True:
#             f_command[i] = int(f_command[i])
#         else:
#             I.append(i)
#     I.append(len(f_command))
#     for i in range(N_1):
#         for j in range(i+1):
#             r_command[i] = f_command[I[j]:I[j+1]]
#     for i in range(N_1):
#         if r_command[i][0] == 'I':
#             for j in range(len(r_command[i][3:])):
#                 origin_pwd.insert(r_command[i][1]+j, r_command[i][3+j])
#         elif r_command[i][0] =='D':
#             for j in range(r_command[i][2]):
#                 origin_pwd.pop(r_command[i][1])
#     print(f"#{test_case + 1} {' '.join(map(str , origin_pwd[:10]))}")
        
# 1230. 암호문 3

# for test_case in range(10):
#     N = int(input())
#     origin_pwd = list(map(int, input().split()))
#     N_1 = int(input())
#     f_command = list(map(str, input().split()))
#     r_command = [[]for i in range(N_1)]
#     I = []
#     for i in range(len(f_command)):
#         if f_command[i].isdigit() == True:
#             f_command[i] = int(f_command[i])
#         else:
#             I.append(i)
#     I.append(len(f_command))
#     for i in range(N_1):
#         for j in range(i+1):
#             r_command[i] = f_command[I[j]:I[j+1]]
#     for i in range(N_1):
#         if r_command[i][0] == 'I':
#             for j in range(len(r_command[i][3:])):
#                 origin_pwd.insert(r_command[i][1]+j, r_command[i][3+j])
#         elif r_command[i][0] =='D':
#             for j in range(r_command[i][2]):
#                 del origin_pwd[r_command[i][1]]
#         else:
#             for j in range(r_command[i][1]):
#                 origin_pwd.append(r_command[i][2+j])
#     print(f"#{test_case + 1} {' '.join(map(str , origin_pwd[:10]))}")

    # 1234. 비밀번호

# a = ['00'] + [str(i*11)for i in range(1, 10)]    
# def pwd_create(n):
#     for i in a:
#         if i in n:
#             n = n.replace(i,'',1)
#             return pwd_create(n)
#     for i in range(len(n)-2):
#         if n[i] != n[i+1] and n[i+1] != n[i+2]:
#             return n
# for test_case in range(10):
#     N, pwd = map(str, input().split(' '))
#     print(f"#{test_case + 1} {pwd_create(pwd)}")


# 5986
# def prime(number):
#     a = [False, False] + [True] * (number-1)
#     for (i, e) in enumerate(a):
#         if e:
#             k = i * 2
#             while k <= n:
#                 a[k] =False
#                 k += i
#     return [x for (x, y) in enumerate(a) if y]

# for t in range(int(input())):
#     n = int(input())
#     a = prime(n)
#     cnt = 0
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             for k in range(j,len(a)):
#                 if a[i] + a[j] + a[k] == n:
#                     cnt+=1
#                 else:
#                     continue
           
#     print(f"#{t+1} {cnt}")

# 5607
# for t in range(int(input())):
#     n, r = map(int, input().split())
#     a = 1
#     b = 1
#     for i in range(r):
#         a *= (n-i)
#     for i in range(r):
#         b *= (r-i)
#     result = a//b
#     if result < 1234567891:
#         print(f"#{t+1} {result}")
#     else:
#         print(f"#{t+1} {result%1234567891}")
# 승률
# T = int(input())
# g = []
# for t in range(T):
#     a,b,c,d = map(int, input().split())
#     e = a / b
#     f = c / d
#     if e < f:
#         g.append("BOB")
#     elif e > f:
#         g.append("ALICE")
#     else:
#         g.append("DRAW")
    
# for t in range(T):
#     print(f"#{t+1} {g[t]}")

#4522
for t in range(int(input())):
    a = list(input())
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            if a[i] == '?' or a[-1-i] == '?':
                continue
            else:
                print(f"#{t+1} Not exist")
                break
    print(f"#{t+1} Exist")
