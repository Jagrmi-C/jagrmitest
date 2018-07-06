def sol(arr):
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

    return leader


def solution(arr):
    count = 0
    if len(arr) < 1:
        return 0
    if len(arr) == 2 and arr[0] == arr[1]:
        return 1
    for ind in range(len(arr)-1):
        # print(arr[:ind+1], arr[ind+1:])
        if sol(arr[:ind+1]) == sol(arr[ind+1:]) and sol(arr[:ind+1]) != -1:
            count += 1
            # print(count)
        else:
            continue
    return count


arr1 = [4, 3, 4, 4, 4, 2]
arr2 = [4, 5, 6, 7, 5, 8, 3, 5, 5, 5, 5]
arr3 = []
arr4 = [4, 3, 4, 4, 4, 2]
print(solution(arr=arr1))
print(solution(arr=arr2))
print(solution(arr=arr3), "Andwer - 0")
print(solution(arr=arr4), "Andwer - 2")


# For example, for the input [0, 0] the solution returned a wrong answer (got 0 expected 1).
print(solution([0, 0]), "Andwer - 1")
# For example, for the input [1, 2, 3, 4, 5] the solution returned a wrong answer (got 3 expected 0).
print(solution([1, 2, 3, 4, 5]), "Andwer - 0")

# For example, for the input [4, 4, 2, 5, 3, 4, 4, 4] the solution returned a wrong answer (got 2 expected 3).
print(solution([4, 4, 2, 5, 3, 4, 4, 4]), "Andwer - 3")


arr8 = [4, 4, 2, 5, 3, 4, 4, 4]
print(solution(arr8))

arr9 = [4, 3, 4, 4, 4, 2]
print(solution(arr9))
