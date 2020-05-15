def m_sort(a):
    if len(a) <= 1:
        return a
    center = len(a) // 2
    right = m_sort(a[center:])
    left = m_sort(a[:center])
    
    return merge(left, right)

def merge(left,right):
    global cnt
    n_right = len(right)
    n_left = len(left)
    i = 0
    i_right = 0
    i_left = 0
    result = [0] * (n_right+n_left)
    if left[-1] > right[-1]:
        cnt += 1
    while i_right != n_right and i_left != n_left:
        if right[i_right] >= left[i_left]:
            result[i] += left[i_left]
            i += 1
            i_left += 1
        else:
            result[i] += right[i_right]
            i += 1
            i_right += 1
    if i_left != n_left:
        while i_left != n_left:
            result[i] += left[i_left]
            i += 1
            i_left += 1
    if i_right != n_right:
        while i_right != n_right:
            result[i] += right[i_right]
            i += 1
            i_right += 1
    return result

for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    result_ = m_sort(a)
    print(f"#{t+1} {result_[n//2]} {cnt}")