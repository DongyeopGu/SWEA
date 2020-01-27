T = int(input())
for test_case in range(T):
    N, M = map(int, input().split(' '))
    fly_num = []
    sum_fly = 0
    max_fly = 0
    for n in range(N):
        fly = list(map(int, input().split(' ')))
        fly_num.append(fly)
    count = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            for k in range(M):
                for l in range(M):
                    sum_fly += fly_num[i + k][j + l]
                    count += 1
                    if count > M**2:
                        count = 1
                        sum_fly = fly_num[i + k][j + l]
                    if sum_fly > max_fly:
                        max_fly = sum_fly

    print(f"#{test_case+1} {max_fly}")