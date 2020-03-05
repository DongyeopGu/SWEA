for t in range(int(input())):
    N = int(input())
    a = list(map(int, input().split()))
    sum_score = {0}
    for i in a:
        for j in list(sum_score):
            sum_score.add(j+i)
    print(f"#{t+1} {len(sum_score)}")