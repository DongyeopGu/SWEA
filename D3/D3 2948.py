# 2948
# for t in range(int(input())):
#     N, M = map(int,input().split())
#     set_1 = set(input().split())
#     set_2 = set(input().split())
#     result = set_1&set_2
#     print(f"#{t+1} {len(result)}")

# 3131
def prime(n):
    a = [False, False] + [True] * (n - 1) 
    for k in range(2, int(n ** 0.5 + 1.5)):
        if a[k]: 
            a[k*2::k] = [False] * ((n - k) // k) 
    return [x for x in range(n+1) if a[x]]
print(' '.join(map(str, prime(10**6))))