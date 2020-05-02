# 4406
for t in range(int(input())):
    a = list(input())
    for i in ['a','e','i','o','u']:
        for j in range(len(a)):
            if i == a[j]:
                a[j]=''
    print(f"#{t+1} {''.join(map(str, a))}")
# 4751.
for t in range(int(input())):
    a = list(input())
    n = (len(a) * 4) + 1
    b = ['.','.','#','.']*(n//4)+['.']
    c = ['.','#']*(n//2)+['.']
    d = ['#','.']*(n//2)+['#']
    print(''.join(b))
    print(''.join(c))
    for i in range(len(a)):
        d[4*i+2]=a[i]
    print(''.join(d))
    print(''.join(c))
    print(''.join(b))
#4047
for t in range(int(input())):
    a=input()
    b=[]
    c=1
    d=[a.count("S"),a.count("D"),a.count("H"),a.count("C")]
    for i in range(0,len(a),3):
        b.append(a[i:i+3])
    if len(set(b))<len(b):
        c=0
        print(f"#{t+1} ERROR")
    else:
        print(f"#{t+1} {13-d[0]} {13-d[1]} {13-d[2]} {13-d[3]}")

# 5356.
T=int(input())
for tc in range(1, T+1):
    arr = [input() for _ in range(5)]
    l = [len(i) for i in arr]  # 각 문자열의 길이
    ml = max(l) # 문자열 중 최대길이
 
    temp = ""
    for i in range(ml):
        for j in range(5):
            if l[j] > i:  # 자신의 문자열의 길이보다 열번호가 작으면 문자 추가하지 않음
                temp += arr[j][i]
    print("#%d %s"%(tc, temp))         
# 5431.
for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    n_li = list(range(1,n+1))
    for i in a:
        if i in n_li:
            n_li.remove(i)
    print(f"#{t+1} {' '.join(map(str, n_li))}")
4466.
for t in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(a,reverse=True)
    result = sum(b[:k])
    print(f"#{t+1} {result}")
# 5549.
for t in range(int(input())):
    a = input()
    if int(a[-1])%2 == 0:
        print(f"{t+1} Even")
    else:
        print(f"{t+1} Odd")