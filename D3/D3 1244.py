#1244. 최대상금 다시하기

def maxprize(a, b, z, N):
    if a == b:
        str_N = list(map(str, N))
        int_N = int(''.join(str_N))
        global max_N
        if max_N < int_N:
            max_N = int_N
        return
    else:
        f_N = N[z]
        new_li = N[z + 1:]
        max_N = max(new_li)
        if max_N > f_N:
            for i in range(len(new_li)):
                if new_li[i] == max_N:
                    a_li = N
                    a_li[z], a_li[i+z+1] = a_li[i+z+1], a_li[z]
                    maxprize(a, b+1, z+1, N)
        else:
            if zero == len(N) - 2:
                if len(set(N)) < len(N):
                    maxprize(a,a, z+1, N)
                    return
                else:
                    if (a-b)%2 == 0:
                        maxprize(a,a,z+1,N)
                        return
                    else:
                        N[-1], N[-2] = N[-2], N[-1]
                        maxprize(a,a,z+1,N)
                        return
            else:
                maxprize(a,b,zero+1,N)

for test_case in range(int(input())):
    N, M = map(int, input().split())
    N_li = list(map(int, str(N)))
    cnt = 0
    max_N = -1
    if int(M) % 2 == 0 and N_li == sorted(N_li, reverse=True):
        print(f"#{test_case + 1} {''.join(map(str, N_li))}")
    elif int(M) % 2 == 1 and N_li == sorted(N_li, reverse=True):
        N_li[-1], N_li[-2] = N_li[-2], N_li[-1]
        print(f"#{test_case + 1} {''.join(map(str, N_li))}")
    else:
        print(maxprize(M, cnt, 0, N))
    
        

        
    