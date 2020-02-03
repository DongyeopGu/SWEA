# 1289. 원재의 메모리 복구
for test_case in range(int(input())):
    N = list(map(int, ' '.join(input().split())))
    cnt = 0
    a = 0
    if N[0] == 1:
        cnt = 1
    else:
        cnt = 0
    for i in range(1,len(N)):
        if N[i] != N[i-1]:
            cnt += 1
        else:
            cnt += 0
    print(f"#{test_case + 1} {cnt}")
