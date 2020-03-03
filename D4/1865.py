def solv(per, sum_val, a=0):
    global result
    if sum_val <= result:
        return
    if per == n:
        if sum_val > result:
            result = sum_val
        return
    for i in range(a,n):
        n_list[i],n_list[a] = n_list[a], n_list[i]
        solv(per+1,sum_val*p[a][n_list[a]]/100,a+1)
        n_list[i],n_list[a] = n_list[a], n_list[i]
    
for t in range(int(input())):
    n = int(input())
    n_list = list(range(n))
    p = [list(map(int, input().split()))for _ in range(n)]
    result = 0
    solv(0,1)
    print(f"#{t+1} {100*result:.6f}")