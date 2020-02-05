# 2948
# for t in range(int(input())):
#     N, M = map(int,input().split())
#     set_1 = set(input().split())
#     set_2 = set(input().split())
#     result = set_1&set_2
#     print(f"#{t+1} {len(result)}")

# 3131
a = set(range(2,10**6+1))
for i in range(2,10**6+1):
    if i in a:
        a -= set(range(2*i,10**6+1,i))

