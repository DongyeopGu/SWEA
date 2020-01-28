for test_case in range(int(input())):
    N = int(input())  
    print(f"#{test_case + 1}")
    for i in range(N):
        a = 1
        pascal = [a]
        print('1', end=' ')
        for j in range(i):
            a = a * (i - j) / (j + 1)
            pascal.append(a)
            print(int(a), end=' ')
        print()  