def golden_max_slice(arr):
    max_ending = max_slice = 0
    for a in arr:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        print(max_ending, max_slice)
    return max_slice


a = [5, -7, 3, 5, -2, 4, -1]
print(golden_max_slice(arr=a))
