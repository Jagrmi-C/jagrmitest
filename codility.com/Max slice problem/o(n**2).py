def qudratic_max_clice(arr):
    n = len(arr)
    result = 0
    for p in range(n):
        sum = 0
        for q in range(p, n):
            # print(p, q)
            sum += arr[q]
            result = max(result, sum)
            print(sum, result)
    return result


a = [5, -7, 3, 5, -2, 4, -1]
print(qudratic_max_clice(arr=a))
