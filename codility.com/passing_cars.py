#


def solution(A):
    # write your code in Python 3.6
    n = len(A)

    start = 0
    res = 0
    for i in range(n - 1, -1, -1):
        if A[i] == 0:
            res += start
            if res > 100000000:
                return -1
        else:
            start += 1
    return res

