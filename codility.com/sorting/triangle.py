def solution(ar):
    if len(ar) < 3:
        return 0
    n = len(ar)
    ar.sort()
    for i in range(n-2):
        # By sorting the array, we have guaranteed that P+R>Q
        # and Q+R>P because R is always the biggest
        if ar[i] + ar[i+1] > ar[i+2]:
            return 1
    return 0


ar = [10, 2, 5, 1, 8, 20]  # return 1
print(solution(ar))
