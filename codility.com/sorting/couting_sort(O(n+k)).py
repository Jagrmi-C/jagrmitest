def counting_sort(ar, k):
    n = len(ar)
    count = [0] * (k+1)

    for i in range(n):
        count[ar[i]] += 1

    print(count)

    p = 0

    for i in range(k+1):
        for j in range(count[i]):
            ar[p] = i
            p += 1
    return ar


print(counting_sort([3, 5, 1, 2, 6], 6))
