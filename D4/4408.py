for t in range(int(input())):
    room = [0] * 200
    n = int(input())
    a = [list(map(int, input().split()))for _ in range(n)]
    for i in range(n):
        if a[i][0] > a[i][1]:
            a[i][0], a[i][1] = a[i][1], a[i][0]
        
        for j in range((a[i][0]-1)//2,(a[i][1]-1)//2+1):
            room[j] += 1
    print(f"#{t+1} {max(room)}")