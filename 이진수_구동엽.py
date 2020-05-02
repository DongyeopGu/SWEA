for t in range(int(input())):
    n, num = map(str, input().split())
    result = []
    print(f'#{t+1}',end=" ")
    for a in num:
        b = '0x'+ a.lower()
        hex_num = int(a, 16)
        print("{0:b}".format(hex_num).zfill(4), end="")
    print()