# def quick_sort(a):
#     if len(a) <= 1:
#         return a
#     pivot = a[len(a)//2]
#     left, right, equal =[],[],[]
#     for i in a:
#         if i < pivot:
#             left.append(i)
#         elif i > pivot:
#             right.append(i)
#         else:
#             equal.append(i)
#     return quick_sort(left) + equal + quick_sort(right)

def quick_sort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, r)

def partition(a, l, r):
    pivot = (l + r) // 2
    while l < r :
        while(a[l] < a[pivot] and l < r):
            l += 1
        while(a[r] >= a[pivot] and l < r):
            r -= 1
        if l < r:
            if l == pivot:
                pivot = r
            a[l], a[r] = a[r], a[l]
    A[pivot], a[r] = a[r], a[pivot]
    return r

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    quick_sort(a, 0, n-1)
    print(f"#{t+1} {a[n//2]}")