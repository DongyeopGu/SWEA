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
        field.append(a)
        for j in range(len(a)):
            if a[j] in move_symbol:
                startpoint[0] = i
                startpoint[1] = j
                startpoint[2] = move_symbol.index(a[j])
                field[i][j] = '.'
    N = int(input())
    commandline = list(input())
    for i in commandline:
        move_index = move_command.index(i)
        if move_index < 4:
            i_idx = startpoint[0] + move_dir[move_index][0]
            j_idx = startpoint[1] + move_dir[move_index][1]
            if 0 <= i_idx < H and 0 <= j_idx < W:
                if field[i_idx][j_idx] == '.':
                    startpoint[0] = i_idx
                    startpoint[1] = j_idx
            startpoint[2] = move_index
        else:
            n = startpoint[0]
            m = startpoint[1]
            while True:
                n += move_dir[startpoint[2]][0]
                m += move_dir[startpoint[2]][1]
                if 0 <= n < H and 0 <= m < W:
                    if field[n][m] == "#":
                        break
                    elif field[n][m] == "*":
                        field[n][m] = "."
                        break
                else:
                    break
    field[startpoint[0]][startpoint[1]] = move_symbol[startpoint[2]]
    print(f"#{t+1}",end=' ')
    for i in range(H):
        print(f"{''.join(field[i])}")