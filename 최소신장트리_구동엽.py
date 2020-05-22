def prim(a):
    key = [float('inf')for _ in range(v+1)]
    pi = [None for _ in range(v+1)]
    visit = [0 for _ in range(v+1)]
    key[0] = 0
    for _ in range(v+1):
        min_key =float('inf')
        start = -1
        for i in range(v+1):
            if key[i] < min_key and not visit[i]:
                min_key = key[i]
                start = i
        visit[start] = 1
        for V, W in a[start]:
            if W < key[V] and not visit[V]:
                key[V] = W
                pi[V] = start
    return sum(key)

for t in range(int(input())):
    v, e = map(int, input().split())
    graph = {}
    for _ in range(e):
        n1, n2, weight = map(int, input().split())
        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()
        graph[n1].add((n2, weight))
        graph[n2].add((n1, weight))
    print(f"#{t+1} {prim(graph)}")