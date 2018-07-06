def solution(ar):
    if len(ar) < 3:
        return -1
    ar.sort()
    return max((ar[-1] * ar[-2] * ar[-3]), (ar[0] * ar[1] * ar[-1]))


ar = [-3, 1, 2, -2, 5, 6]
print(solution(ar))
ar = [-3, 1]
print(solution(ar))
ar = [-3, 1, 0]
print(solution(ar))
ar = [-3, 1, 2, 0]
print(solution(ar))
ar = [-3, 1, 2, -2, 5, 6]
print(solution(ar))

ar = [-2, -3, -5, -6, 0]  # Returned 0
print(solution(ar))
