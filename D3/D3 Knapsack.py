for t in range(int(input())):
    N, K = map(int,input().split())
    sack_li = []
    for i in range(N):
        sack_li.append(list(map(int, input().split())))
    v_li = []
    c_li = []
    sum_li = []
    s_li = []
    for i in range(N):
        v_li.append(sack_li[i][0])
        c_li.append(sack_li[i][1])
    for i in range(1<<len(v_li)):
        for j in range(len(v_li)):
            if i & (1<<j):
                sum_li.append(v_li[j])
        if sum(sum_li) == K:
            s_li.append(sum_li)
        sum_li = []
    