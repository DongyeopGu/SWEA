from collections import deque

def sol(start, end):
    check = {}
    check[start] = end
    while q:
        num, cnt = q.popleft()
        if num == end:
            return cnt
        if num > 1000000 or num <= 0:
            continue
        for i in range(4):
            a = 0
            if i == 0:               
                a = num + 1
                if a not in check:
                    q.append((a, cnt+1))
                    check[a] = 1
            elif i == 1:
                a = num - 1
                if a not in check:
                    q.append((a, cnt+1))
                    check[a] = 1
            elif i == 2:
                a = num * 2
                if a not in check:
                    q.append((a, cnt+1))
                    check[a] = 1
            elif i == 3:
                a = num - 10
                if a not in check:
                    q.append((a, cnt+1))
                    check[a] = 1
            
for t in range(int(input())):
    n, m = map(int, input().split())
    q = deque()
    q.append([n, 0])    # 시작과 카운트 입력
    result = sol(n, m)
    print(f"#{t+1} {result}")