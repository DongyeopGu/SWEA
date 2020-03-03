dt = [(1,0), (0,1), (-1,0), (0,-1)]
for t in range(int(input())):
    n = int(input())
    room = [list(map(int, input().split()))for _ in range(n)]
    max_value = 0
    result = n ** 2 + 1
    for i in range(n):
        for j in range(n):
            start_num = room[i][j]
            cnt = 1
            while True:
                for delta in dt:
                    dx, dy = i + delta[0], j + delta[1]
                    if 0 <= dx < n and 0 <= dy < n and room[dx][dy] - room[i][j] == 1:
                        cnt += 1
                        i, j = dx, dy
                        break
                else:
                    break
            if cnt > max_value:
                max_value = cnt
                result = start_num
            elif cnt == max_value and start_num < result:
                max_value = cnt
                result = start_num
    print(f"#{t+1} {result} {max_value}")