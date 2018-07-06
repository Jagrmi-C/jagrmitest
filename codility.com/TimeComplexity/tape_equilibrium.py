def solution(a):
    if len(a) < 2:
        return -1
    first = a[0]
    last = sum(a) - a[0]
    min_diff = abs(first - last)
    for i in range(1, len(a) - 1):
        num = a[i]
        first += num
        last -= num
        min_diff = min(abs(first - last), min_diff)
    return min_diff


a = [3, 1, 2, 4, 3]
print(solution(a))
a = [1, ]
print(solution(a))

