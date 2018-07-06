def solution(x, y, d):
    if y < x or d <= 0:
        raise Exception("Invalid argument")
    if (y - x) % d ==0:
        return (y - x) // d
    else:
        return (y - x) // d + 1


print(solution(10, 85, 30))
print(solution(10, 10, 2))
# print(solution(10, 5, 30))
# print(solution(10, 85, -30))
