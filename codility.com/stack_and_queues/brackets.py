def solution(array):
    if len(array) == 0:
        return 1

    if len(array) % 2 == 1:
        return 0

    to_push = ["{", "(", "["]
    selection = {
        "}": "{",
        ")": "(",
        "]": "["
    }

    a = []
    # if array[0] not in to_push:
    #     return 0

    for i in array:
        if len(a) == 0 and i not in to_push:
            return 0
        # print(i, a)
        if i in to_push:
            a.append(i)

        elif a[-1] != selection[i]:
            # print("OOPS")
            return 0
        else:
            a.pop()
    if len(a) == 0:
        return 1
    else:
        return 0


S = "{[()()]}"
# return 1
print(solution(S))
S1 = "([)()]"
# return 0
print(solution(S1))
S2 = ""
# return 1
print(solution(S2))
S3 = "{{{{"
# return 0
print(solution(S3))
S4 = "())(()"
print(solution(S4))
# return 0
# 1 0 1 0 0