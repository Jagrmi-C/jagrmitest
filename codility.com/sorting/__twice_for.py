ar = [1, 4, 7, 2, 6]

for i in range(5):
    for k in range(i+1, 5):
        print(i, k)

print("array")
n = len(ar)
for i in range(n):
    for k in range(i, n):
        print(ar[i], ar[k])
