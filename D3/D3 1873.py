# 1873. 상호의 배틀필드
for t in range(int(input())):
    H, W = map(int, input().split())
    move_symbol = ["^", "v", "<", ">"]
    move_command = ["U", "D", "L", "R", "S"]
    move_dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    field = []
    startpoint = [0, 0, 0]
    for i in range(H):
        a = list(input())
        for j in range(W):
            if a[j] in move_symbol:
                startpoint[0] = i
                startpoint[1] = j
                startpoint[2] = move_symbol.index(a[j])
        field.append(a)
    N = int(input())
    commandline = list(input())
    for i in commandline:
        i_index = move_command.index(i)
        if i_index <= 3:
             