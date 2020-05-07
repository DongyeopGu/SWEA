for t in range(int(input())):
    a = list(map(int, input().split()))
    cnt = 0
    flag = False
    for i in range(6, 13, 2):
        result = []
        for j in range(2):
            deck = [a[k]for k in range(j, i, 2)]
            cnt_list = [0]*12
            for m in range(len(deck)):
                cnt_list[deck[m]] += 1
            n = 0
            tri = Run = 0
            while n < 10:
                if cnt_list[n] >= 3:
                    cnt_list[n] -= 3
                    tri += 1
                    continue
                if cnt_list[n] >= 1 and cnt_list[n+1] >= 1 and cnt_list[n+2] >= 1:
                    cnt_list[n] -= 1
                    cnt_list[n+1] -= 1
                    cnt_list[n+2] -= 1
                    Run += 1
                    continue
                n += 1
            cnt += 1

            if tri > 0 or Run > 0:
                result.append(1)
            else:
                result.append(0)

        if result[0] < result[1]:
            flag = True
            print(f"#{t+1} 2")
            break
        elif result[0] > result[1] or ((result[0] == 1 and result[1] == 1) or (result[0] == 2 and result[1] == 2)):
            flag = True
            print(f"#{t+1} 1")
            break
    if flag:
        continue
    else:
        print(f"#{t+1} 0")

            