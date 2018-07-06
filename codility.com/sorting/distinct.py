def solution(ar):
    if len(ar) == 0:
        return 0
    d = 1
    ar.sort()
    for i in range(1, len(ar)):
        if ar[i] == ar[i-1]:
            continue
        else:
            d += 1
    return d


ar1 = []
ar2 = [1]
ar3 = [1, 5, 8, 9]
ar4 = [2, 2, 2, 2, 3, 1]   # Return 3
for i in [ar1, ar2, ar3, ar4]:
    print(solution(i))
