for t in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            if a[i][1] > a[j][1]:
                a[i], a[j] = a[j], a[i]
    result = [a[0]]
    visit = [0]*n
    visit[0] = 1
    while True:
        for i in range(n):
            if result[-1][-1] > a[i][0]:
                visit[i] = 1
        if not 0 in visit:
            break
        idx = 0
        max_value = 100000000
        for i in range(n):
            if visit[i] == 0 and result[-1][-1] <= a[i][0] and a[i][1] < max_value:
                idx = i
                max_value = a[i][0]
        result.append(a[idx])
    print(f"#{t+1} {len(result)}")

#     5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
# https://www.dropbox.com/request/rssNLR9dqvyvWYmbz8wH

#  5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
# https://www.dropbox.com/request/6TuJzadSSu8bFMFn8tYE

# 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임
# https://www.dropbox.com/request/22hkK2tLtNTluEww6T0x
