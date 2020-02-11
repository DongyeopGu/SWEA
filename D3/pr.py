a = list(map(str, input().upper()))
b = list(set(a))
cnt = []
for i in b:
    cnt.append(a.count(i))
if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(b[cnt.index(max(cnt))])
 