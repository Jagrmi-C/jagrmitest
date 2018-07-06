def solution(a):
    if len(a) == 0:
        return 1
    elif len(a) == 1:
        if a[0] == 1:
            return 2
        else:
            return 1
    else:
        a.sort()

        for i in range(len(a)):
            if a[i] != i+1:
                return i+1
        return len(a)+1


a = [2, 3, 1, 5]
print(solution(a))
a = []
print(solution(a))
a = [1, ]
print(solution(a))
a = [1, 3, 2, 4]
print(solution(a))
