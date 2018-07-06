def show_max_clice(arr):
    n = len(arr)
    result = 0
    for p in range(n):
        for q in range(p, n):
            sum = 0
            for i in range(p, q+1):
                sum += arr[i]
            result = max(result, sum)
    return result


a = [5, -7, 3, 5, -2, 4, -1]
print(show_max_clice(arr=a))
