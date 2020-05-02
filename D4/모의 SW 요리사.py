for t in range(int(input())):
    n = int(input())
    s = [list(map(int, input().split()))for _ in range(n)]
    result=[]
    result_1 = []
    for i in range(n):
        for j in range(n):
            if i != j:
                result.append(s[i][j])
    for j in range(n):
        for i in range(n):
            if i != j:
                result_1.append(s[i][j])
    result_2 = [0 for _ in range(len(result))]
    for i in range(len(result)):
        result_2[i] = result[i]+result_1[i]
    print(result_2)