# weight = [3, 5, 7]
# n = len(weight)
# a = 6
#
# for i in range(n):
#     print(weight)
#     if weight[i] < a:
#         weight.remove(weight[i])
#
# print(weight)

# arr8 = [4, 3, 4, 4, 4, 2]
#
# print('start')
# for i in range(len(arr8) - 1):
#     print(arr8[:i+1], arr8[i+1:], " - ", i)


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
        return 0
    print("Leader - ", leader)
    print("Count - ", arr.count(leader))

    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(len(arr)):
        if arr[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index + 1) // 2 and \
                arr.count(leader) - leader_count_so_far > (len(arr) - index - 1) // 2:
            equi_leaders += 1

    return equi_leaders


a = [2, 5, 5, 4, 4, 4]
b = [3, 4]
arr4 = [4, 3, 4, 4, 4, 2]
print(solution(arr4), "Answer - 2")
print(solution([1, 2, 3, 4, 5]), "Andwer - 0")
print(solution([1, 2]), "Answer - 0")