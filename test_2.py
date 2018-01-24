n = 99999
a = [0] * n
for i in range(n):
    a[i] = i
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n, i):
            print(j)
            a[j] = 0
    i += 1
# print(lst)
