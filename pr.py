T = int(input())  # 테스트 케이스
for i in range(T):    # 테스트 케이스 반복
    N = int(input())  # 테스트 1<= N <= 10
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
            pascal_n = pascal_    
            pascal_n[k] = pascal_[k] + pascal_[k-1]
            print(k, pascal_n)


