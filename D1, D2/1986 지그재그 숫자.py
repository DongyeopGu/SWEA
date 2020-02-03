T = int(input())
for test_case in range(T):
    N = int(input())
    result = 0
    for i in range(1, N+1):
        result += -i * ((-1)**i)
    print(f"#{test_case+1} {result}")