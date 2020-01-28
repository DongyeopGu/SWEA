for test_case in range(int(input())):
    N = int(input())  
    print(f"#{test_case + 1}")
    pascal_1 = [1]
    pascal_2 = [1, 1]
    pascal_ = [1, 1]
    if N == 1:
        print(''.join(map(str, pascal_1)))
    elif N == 2:
        print(''.join(map(str, pascal_1)))
        print(' '.join(map(str, pascal_2)))
    else:
        print(''.join(map(str, pascal_1)))
        print(' '.join(map(str, pascal_2)))
        pascal_n = [1] * N
        for k in range(1, N-1):
            pascal_n[k] = pascal_[k] + pascal_[k-1]
            print(k, pascal_n)


  
    