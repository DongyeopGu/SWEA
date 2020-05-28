for test_case in range(int(input())):
    N, M = map(int, input().split())
    pwd_ch = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    pwd_li = str()
    pwd = str()
    change_pw = []
    for i in range(N):
        a = input()
        if '1' in a:
            pwd_li = a
            continue
    for i in range(1, M):
        if pwd_li[-i] == '1':
            pwd = ''.join(reversed(pwd_li[-i:-i-56:-1]))
            break
    for i in range(8):
        for j in range(10):
            if pwd[i*7:i*7+7] == pwd_ch[j]:
                change_pw.append(j)
                
    if len(change_pw) == 8:
        if ((change_pw[0] + change_pw[2] + change_pw[4] + change_pw[6]) * 3 + (change_pw[1] + change_pw[3] + change_pw[5]) + change_pw[7]) % 10 == 0:
            print(f"#{test_case + 1} {sum(change_pw)}")
        else:
            print(f"#{test_case + 1} {0}")
    else:
        print(f"#{test_case + 1} {0}")