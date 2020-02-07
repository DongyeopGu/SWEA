# 3260 두수덧셈
# for t in range(int(input())):
    # a, b = map(int, input().split())
    # print(f"#{t+1} {a+b}")

# 3304 최장 공통부분
# def lcs(a,b):
#     arr = [[0 for _ in range(len(b)+2)]for _ in range(len(a)+2)]
#     for i in range(1,len(a)+1):
#         for j in range(1,len(b)+1):
#             if a[i-1] == b[j-1]:
#                 arr[i][j] = arr[i-1][j-1]+1
#             else:
#                 arr[i][j] = max(arr[i-1][j],arr[i][j-1])
#     return arr[len(a)][len(b)]

# for t in range(int(input())):
#     a, b = map(str, input().split())
#     print(f"#{t+1} {lcs(a,b)}")

# 3307 최장 증가 부분
def lis(a):
    d = [0] * (N)
    for i in range(1,N):    
        for j in range(i):
            if a[i] > a[j]:
                d[i] = max(d[i],d[j]+1)
    return max(d)

for t in range(int(input())):
    N = int(input())
    a_list = list(map(int, input().split()))
    print(f"#{t+1} {lis(a_list)+1}")
