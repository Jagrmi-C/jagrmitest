def solution(arr):
    size = 0
    value = 0
    for i in range(len(arr)):
        if size == 0:
            value = arr[i]
            size += 1
        else:
            if value != arr[i] and size != 0:
                size -= 1
            else:
                size += 1
    leader = value
    if arr.count(leader) <= len(arr) // 2:
        return -1

    return arr.index(leader)


arr1 = [4, 5, 6, 7, 5, 8, 3, 5, 5, 5, 5]
print(solution(arr=arr1))

arr2 = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(arr=arr2))

arr3 = [3, 4, 1, 2, 3, -1, 3, 9]
print(solution(arr=arr3))

arr4 = [3, ]
print(solution(arr=arr4))

arr5 = []
print(solution(arr=arr5))
