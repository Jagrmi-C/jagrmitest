import time

n = 99999
lst = [2]
start = time.time()
for i in range(3, n + 1, 2):
    if (i > 10) and (i % 10 == 5):
        continue
    for j in lst:
        if j*j-1 > i:
            lst.append(i)
            break
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
print(- start + time.time())

