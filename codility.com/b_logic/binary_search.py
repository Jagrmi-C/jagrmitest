def bin_search(a, x):
    left = 0
    right = len(a) - 1
    middle = right//2
    while a[middle] != x and left < right:
        if x > a[middle]:
            left = middle + 1
        else:
            right = middle - 1
    if left > right:
        return "There is no such value"
    else:
        return middle


def bin_search_virt(a, x):
    n = len(a)
    if n == 0:
        return -1
    left = 0
    right = n - 1
    while left < right:
        middle = (left + right)//2

        if x > a[middle]:
            left = middle + 1
        else:
            right = middle
    if a[left] == x:
        return left
    return -1


a1 = [1, 2, 5, 9, 9]
x1 = 5
print(bin_search_virt(a1, x1))

a2 = []
x2 = 5
print(bin_search_virt(a2, x2))

a3 = [1, 2, 5, 9, 9]
x3 = 1
print(bin_search_virt(a3, x3))

a4 = [1, 2, 5, 9, 9]
x4 = 9
print(bin_search_virt(a4, x4))
