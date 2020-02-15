# def dfs(a,b):
#     check[a] = 1
#     result.append(b)
#     for i in arr[a]:
#         if check[i] == 0:
#             dfs(i,b+1)
#             check[i] = 0


# for t in range(int(input())):
#     n, m = map(int, input().split())
#     arr = [[]for _ in range(n)]
#     result = []
#     for i in range(m):
#         a,b = map(int, input().split())
#         arr[a-1].append(b-1)
#         arr[b-1].append(a-1)
#     for i in range(n):
#         check = [0] * n
#         c = 1
#         dfs(i,c)
#         result.append(c)
#     print(f"#{t+1} {max(result)}")

def dfs(a,b):
    visit[a] = 1
    result.append(b)
    for i in node[a]:
        if visit[i] == 0:
            dfs(i,b+1)
            visit[i] = 0

for t in range(int(input())):
    n, m = map(int, input().split())
    node = dict()
    for i in range(1,n+1):
        node[i] = []
    for i in range(m):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    result = []
    for i in range(1,n+1):
        visit = [0] * (n+1)
        c = 1
        dfs(i,c)
        result.append(c)
    print(f"#{t+1} {max(result)}")
