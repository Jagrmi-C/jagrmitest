a = [4, 2, 2, 5, 1, 5, 8]
n = len(a)

res_list = []
for i in range(n):
    for j in range(i + 1, n):
        res_list.append(sum(a[i:j+1]) / (j - i + 1))
        print(f"{i} - i, "
              f"{j} - j, "
              f"slice - a[{i}:{j+1}] - {a[i:j+1]},",
              f"sum - {sum(a[i:j+1])}, {(j - i + 1)}")
res = min(res_list)
print(res)
