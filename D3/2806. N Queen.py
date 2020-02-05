# N Queen Problem
def placeQueen(queen_pos):
    cnt = 0
    n = len(queen_pos)
    if n == N:
        return 1
    for i in range(N):
        for j in range(n):
            if i == queen_pos[j]:
                break
            if n - j == i - queen_pos[j]:
                break
            if n - j == queen_pos[j] - i:
                break
        else:
            cnt += placeQueen(queen_pos + [i])
    return cnt
for t in range(int(input())):
    N = int(input())
    print(f"#{t+1} {placeQueen([])}")
