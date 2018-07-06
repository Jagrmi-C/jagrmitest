def solution(a):
    n = len(a)
    if n < 2:
        return 0

    range_u, range_l = [0]*n, [0]*n
    for i in range(n):
        range_u[i] = i + a[i]
        range_l[i] = i - a[i]

    range_u.sort()
    range_l.sort()

    range_lower_i = 0
    count = 0
    for range_upper_i in range(n):
        while range_lower_i < n and range_u[range_upper_i] >= range_lower_i[range_lower_i]:
            range_lower_i += 1
        count += range_lower_i - range_upper_i - 1
        print(count)

    return range_u, range_l


a = [1, 5, 2, 1, 4, 0]
print(solution(a))
# a2 = [1, 1, 1]  # solution 3
# print(solution(a2))
# a3 = []  # solution 0
# print(solution(a3))
