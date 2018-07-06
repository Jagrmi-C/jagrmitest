def solution(arr):
    max_ending = max_slice = arr[0]
    for a in arr[1:]:
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


