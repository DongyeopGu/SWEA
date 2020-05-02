# 3456
for t in range(int(input())):
    a = list(map(int, input().split()))
    for i in range(3):
        if a.count(a[i])%2==1:
            print(f"#{t+1} {a[i]}")
            break

# 3499 퍼펙트 셔플
for t in range(int(input())):
    N = int(input())
    card = list(map(str, input().split()))
    print(f"#{t+1}",end=' ')
    if len(card) % 2 == 0:
        for i in range(N//2):
            print(f"{card[i]} {card[N//2+i]}",end=" ")
        print()
    else:
        for i in range(N//2):
            print(f"{card[i]} {card[N//2+i+1]}",end=" ")
        print(f"{card[N//2]}",end=" ")
        print()

# 3750 Digit sum
for t in range(int(input())):
    print(f"#{t+1} {(int(input())-1)%9+1}")
    
    