def prefix_sums(a):
    n = len(a)
    p = [0]*(n + 1)
    print(p, n)
    for k in range(1, n + 1):
        p[k] = p[k - 1] + a[k - 1]
    return p


a_list = [4, 2, 2, 5, 1, 5, 8]
print(prefix_sums(a_list))
