ar = [10, 2, 5, 1, 8, 20]
n = len(ar)

for p in range(n):
    for q in range(p + 1, n):
        for r in range(q + 1, n):
            print(ar[p], ar[q], ar[r])
