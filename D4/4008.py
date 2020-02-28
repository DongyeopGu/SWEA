# def cal(i, numbs):
#     global max_value, min_value
#     if i == n:
#         max_value = max(max_value, numbs)
#         min_value = min(min_value, numbs)
#     else:
#         if operator[0] != 0:
#             operator[0] -= 1
#             cal(i+1, numbs + numbers[i])
#             operator[0] += 1
#         if operator[1] != 0:
#             operator[1] -= 1
#             cal(i+1, numbs - numbers[i])
#             operator[1] += 1
#         if operator[2] != 0:
#             operator[2] -= 1
#             cal(i+1, numbs * numbers[i])
#             operator[2] += 1
#         if operator[3] != 0:
#             operator[3] -= 1
#             if numbs < 0 and numbs%numbers[i]:
#                 cal(i+1, numbs//numbers[i]+1)
#             else:
#                 cal(i+1, numbs//numbers[i])
#             operator[3] += 1

# for t in range(int(input())):
#     n = int(input())
#     operator = list(map(int, input().split()))
#     numbers = list(map(int, input().split()))
#     min_value = 100000000
#     max_value = -100000000
#     cal(1,numbers[0])
#     print(f"#{t+1} {max_value - min_value}")

import itertools
import copy

oper = ['+', '-', '*', '//']

for T in range(int(input())):
    N = int(input())
    opr = map(int, input().split())  # 2 1 0 1
    Num = list(map(int, input().split()))  # 3 5 3 7 9
    a = copy.deepcopy(Num)

    choi_oper = []
    for idx, i in enumerate(opr):
        for j in range(i):
            choi_oper += [oper[idx]]

    final_oper = set()
    perm = itertools.permutations(choi_oper)
    for i in perm:
        final_oper.add(i)

    result = []
    for p in final_oper:
        Num = copy.deepcopy(a)
        for j in p:
            if j == '+':
                calc = (Num.pop(0) + Num.pop(0))
                Num.insert(0, calc)
            elif j == '-':
                calc = (Num.pop(0) - Num.pop(0))
                Num.insert(0, calc)
            elif j == '*':
                calc = (Num.pop(0) * Num.pop(0))
                Num.insert(0, calc)
            elif j == '//':
                num1 = Num.pop(0)
                num2 = Num.pop(0)
                if num1 < 0 and num1 % num2:
                    calc = (num1 // num2) + 1
                    Num.insert(0, calc)
                else:
                    calc = (num1 // num2)
                    Num.insert(0, calc)
        result.append(Num[0])

    print("#{} {}".format(T+1, max(result)-min(result)))