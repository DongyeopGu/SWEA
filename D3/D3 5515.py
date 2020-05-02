5515. 2016년 요일 맞추기
for t in range(int(input())):
    m, d = map(int, input().split())
    day = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(m):
        days += day[i]
    print(f"#{t+1} {(days+d+3)%7}")

5162 두가지빵
for t in range(int(input())):
    a, b, c = map(int, input().split())
    result = 0
    if a < b:
        result = c // a
    else:
        result = c // b
    print(f"#{t+1} {result}")

6692 다솔이 월급
for t in range(int(input())):
    N = int(input())
    result = 0
    for i in range(N):
        a, b = map(float, input().split())
        result += a * b
    print(f"{t+1}", "%.6f" % result)

5789. 현주의 상자 바꾸기
for t in range(int(input())):
    n, q = map(int, input().split())
    box = [0 for _ in range(n)]
    for j in range(1,q+1):
        l, r = map(int, input().split())
        for i in range(l-1,r):
            box[i] = j
    print(f"#{t+1} {' '.join(map(str, box))}")

4676. 늘어지는 소리
for t in range(int(input())):
    string = list(input())
    h = int(input())
    idx = list(map(int, input().split()))
    idx_sort =sorted(idx,reverse=True)
    for i in range(len(idx)):
        string.insert(idx_sort[i],'-')
    print(f"#{t+1} {''.join(map(str, string))}")

5603.
for t in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    avg = sum(a)//n
    result = 0
    for i in range(n):
        result += abs(a[i] - avg)
    print(f"#{t+1} {result//2}")

4299
for t in range(int(input())):
    d, h, m = map(int, input().split())
    a = [11, 11, 11]
    result = 0
    if d - a[0] < 0:
        result = -1
    elif a[0] == d:
        if h - a[1] < 0:
            result = -1
        else:
            if m - a[2] < 0:
                result = -1
            else:
                result += (d-a[0]) * 60 * 24
                result += (h-a[1]) * 60
                result += (m-a[2])
    else:
        result += (d-a[0]) * 60 * 24
        result += (h-a[1]) * 60
        result += (m-a[2])
    print(f"#{t+1} {result}")

5948. 새샘이
for t in range(int(input())):
    a = list(map(int, input().split()))
    b = sorted(a,reverse=True)
    cnt = 0
    result = []
    for i in range(7):
        for j in range(i+1,7):
            for k in range(j+1,7):
                result.append(b[i]+b[j]+b[k])
    c = sorted(result,reverse=True)
    v = 0
    for i in range(len(c)-1):
        if c[i] != c[i+1]:
            cnt += 1
        if cnt == 5:
            v = c[i]
            break
    print(f"#{t+1} {v}")

# 5601
for t in range(int(input())):
    n = int(input())
    print(f"#{t+1}",end=' ')
    for i in range(n):
        print(f"1/{n}", end=' ')
    print()