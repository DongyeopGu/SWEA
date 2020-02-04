# 1493. 수의 새로운 연산
for test_case in range(int(input())):
    p, q = map(int, input().split())
    mapping = [[0 for i in range(300)]for j in range(300)]
    a = 1
    p_x = 0
    p_y = 0
    q_x = 0
    q_y = 0
    for i in range(599):
        for j in range(300):
            if 300 > i - j >= 0:
                mapping[i-j][j] = a
                a += 1
    for i in range(300):
        if p in mapping[i]:
            p_y = mapping[i].index(p)
            p_x = i
    for i in range(300):
        if q in mapping[i]:
            q_y = mapping[i].index(q)
            q_x = i
    
    result = mapping[p_x+q_x+1][p_y+q_y+1]
    print(f"#{test_case + 1} {result}")
    