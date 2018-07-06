def solution(arr1, arr2):
    count_alive = 0
    weight = []

    if len(arr1) != len(arr2):
        return 0

    for i in range(len(arr2)):
        if arr2[i] == 0:
            while len(weight) != 0:
                if weight[-1] > arr1[i]:
                    break
                else:
                    weight.pop()
            else:
                count_alive += 1
        else:
            weight.append(arr1[i])
    count_alive += len(weight)
    return count_alive


A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

print(solution(arr1=A, arr2=B))
