def solution(array):
    if len(array) == 0:
        print("len = 0")
        return 1
    if len(array) % 2 == 1:
        print("% 2 == 1")
        return 0

    a = []

    for i in array:
        if len(a) == 0 and i != "(":
            # print("len = 0 and i != (")
            return 0
        # print(i, a)
        if i == "(":
            a.append(i)
        else:
            a.pop()
    if len(a) == 0:
        return 1
    else:
        return 0


S1 = "(()(())())"
print("Correct answer - 1. You - ", solution(S1))

S2 = "())"
print("Correct answer - 0. You - ", solution(S2))