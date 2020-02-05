for t in range(int(input())):
    N = int(input())
    farm = [list(map(int, input()))for i in range(N)]
    base_sum = sum(farm[N//2])
    for i in range(N//2):
        base_sum += sum(farm[i][N//2-i:N//2+i+1])
    for i in range(N//2+1,N):
        base_sum += sum(farm[i][i-N//2:N-(i-N//2)])
    print(f"#{t+1} {base_sum}")