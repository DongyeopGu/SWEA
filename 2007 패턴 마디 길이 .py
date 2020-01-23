T = int(input())
for i in range(T):
    a = list(input())
    result = 0
    for j in range(1, 30):
        if a[0:j] == a[j:j+j]:
            result = j
            break
    print(f"#{i+1} {j}")