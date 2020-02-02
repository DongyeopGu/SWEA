# 1244. 최대상금
for test_case in range(int(input())):
    N = list(map(int, input().split()))
    N_li = list(map(int, str(N[0])))
    
    for i in range(N[1]):
        max_N = N_li.index(max(N_li))
        for j in range(len(N_li)):
            if N_li[0] < max(N_li):
                N_li[0], N_li[max_N] = N_li[max_N], N_li[0]

