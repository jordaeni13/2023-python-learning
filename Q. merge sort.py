def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)

def merge(A, p, q, r):
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1) 

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1

    for k in range(len(tmp)):
        A[p + k] = tmp[k]

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
