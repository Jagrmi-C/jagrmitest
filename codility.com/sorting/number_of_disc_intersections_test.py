def solution(ar):
    c_endpoints = []

    for c, r in enumerate(ar):
        c_endpoints += [(c-r, True), (c+r, False)]

    # print(c_endpoints)
    c_endpoints.sort(key=lambda x: (x[0], not x[1]))
    # print(c_endpoints)
    i, active_circle = 0, 0

    for _, is_begining in c_endpoints:
        if is_begining:
            i += active_circle
            active_circle += 1
        else:
            active_circle -= 1
        if i > 10000000:
            return -1
    return i


ar1 = [1, 5, 2, 1, 4, 0]  # return 11
ar2 = [1, 1, 1]  # solution 3
ar3 = []  # solution 0

print(solution(ar1))
print(solution(ar2))
print(solution(ar3))
