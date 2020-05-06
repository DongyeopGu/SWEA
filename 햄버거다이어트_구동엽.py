for t in range(int(input())):
    n, l = map(int, input().split())
    hamb = [list(map(int, input().split()))for _ in range(n)]
    cal = []
    score = []
    for i in range(n):
        score.append(hamb[i][0])
        cal.append(hamb[i][1])
    board = [[0 for _ in range(l + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, l + 1):
            if cal[i - 1] > j:
                board[i][j] = board[i - 1][j]
            else:
                board[i][j] = max(score[i - 1] + board[i - 1][j - cal[i - 1]], board[i - 1][j])
    print(f"#{t+1} {board[n][l]}")