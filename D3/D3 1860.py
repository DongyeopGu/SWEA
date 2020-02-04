# # 1860 진기의 붕어빵
# for test_case in range(int(input())):
#     N, M, K = map(int, input().split())
#     sec_li = list(map(int, input().split()))
#     for i in range(len(sec_li)):
#         if sorted(sec_li)[i] // M*K < i+1:
#             result =  "Impossible"
#             break
#         else:
#             result = "Possible"
#     print(f"#{test_case + 1} {result}")
for t in range(int(input())):
    N,M,K=map(int,input().split())
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if sorted(a)[i]//M*K<i+1:
            result="Impossible"
            break
        else:
            result="Possible"
    print(f"#{t+1} {result}")