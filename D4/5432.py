for t in range(int(input())):
    a = input()
    b = a.replace('()','-')
    stack = []
    cnt = 0
    for i in b:
        if i == '(':
            cnt += 1
            stack.append(i)
        elif i == ')':
            stack.pop()
        else:
            cnt += len(stack)
    print(f"#{t+1} {cnt}")
