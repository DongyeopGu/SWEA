for t in range(int(input())):
    n, m = map(int, input().split())
    arr1 = sorted(list(map(int, input().split())))
    arr2 = list(map(int, input().split()))
    cnt = 0
    for i in arr2:
        a = 0
        b = n-1
        check = 0
        while a <= b:
            c = (a+b)//2
            if i >= arr1[c]:
                if i == arr1[c]:
                    cnt+=1
                    break
                a = c + 1
                if check == 1:
                    break
                check = 1
            elif i < arr1[c]:
                b = c - 1
                if check == 2:
                    break
                check = 2
    print(f"#{t+1} {cnt}")

