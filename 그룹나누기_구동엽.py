def search(a):
    if a == group[a]:
        return a
    else:
        return search(group[a])
def sol(a, b):
    group[search(b)] = search(a)

for t in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    group = []
    for i in range(1, n+1):
        group.append(i)
    group.insert(0,0)
    # print(group)
    for i in range(m):
        start = arr[2*i]
        end = arr[2*i+1]
        sol(start, end)
    result = []
    for i in range(len(group)):
        result.append(search(i))
    print(f"#{t+1} {len(set(result))-1}")