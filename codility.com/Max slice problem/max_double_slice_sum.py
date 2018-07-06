def solution(arr):
    n = len(arr)
    starts, ends = [0] * n, [0] * n
    # ignore arr[0] and arr[n-1]
    for i in range(1, n-1):
        left, right = i, n - i - 1
        starts[left] = max(starts[left-1] + arr[left], 0)
        ends[right] = max(ends[right+1] + arr[right], 0)
        print(starts, ends)
    return max(starts[i-1] + ends[i+1] for i in range(1, n-1))


a = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(a))
