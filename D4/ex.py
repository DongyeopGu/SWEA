for tc in range(1, int(input())+1):
    n = int(input())
    rooms = [0] * 401
    for i in range(n):
        cr, mr = map(int, input().split())
        for c in range(min(cr, mr)+1, max(cr, mr)+1):
            rooms[c] += 1
    print('#{} {}'.format(tc, max(rooms)))