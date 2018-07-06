def selection_sort(ar):
    n = len(ar)
    for k in range(n):
        minimal = k
        for j in range(k + 1, n):
            if ar[j] < ar[minimal]:
                minimal = j
                print(k, j, minimal, ar)
        ar[k], ar[minimal] = ar[minimal], ar[k]
    return ar


ar = [1, 5, 2, 7, 9, 6]
res = selection_sort(ar)
print("Finally result: ", res)
