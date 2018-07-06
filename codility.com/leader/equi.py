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
    leader_count = len([number for number in arr if number == value])
    if leader_count <= len(arr)//2:
        # The candidate is not the leader
        return 0
    else:
        leader = value

    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(len(arr)):
        if arr[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index + 1) // 2 and \
                leader_count - leader_count_so_far > (len(arr) - index - 1) // 2:
            equi_leaders += 1

    return equi_leaders


arr4 = [4, 3, 4, 4, 4, 2]
print(solution(arr4), "Answer - 2")
print(solution([1, 2, 3, 4, 5]), "Andwer - 0")
print(solution([1, 2]), "Answer - 0")
