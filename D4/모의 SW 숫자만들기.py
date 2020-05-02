def cal(i, numbs):
    global max_value, min_value
    if i == n:
        max_value = max(max_value, numbs)
        min_value = min(min_value, numbs)
    else:
        if operator[0] != 0:
            operator[0] -= 1
            cal(i+1, numbs + numbers[i])
            operator[0] += 1
        if operator[1] != 0:
            operator[1] -= 1
            cal(i+1, numbs - numbers[i])
            operator[1] += 1
        if operator[2] != 0:
            operator[2] -= 1
            cal(i+1, numbs * numbers[i])
            operator[2] += 1
        if operator[3] != 0:
            operator[3] -= 1
            if numbs < 0 and numbs%numbers[i]:
                cal(i+1, numbs//numbers[i]+1)
            else:
                cal(i+1, numbs//numbers[i])
            operator[3] += 1

for t in range(int(input())):
    n = int(input())
    operator = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    min_value = 100000000
    max_value = -100000000
    cal(1,numbers[0])
    print(f"#{t+1} {max_value - min_value}")