# def solution(a):
#     right, total = 0, 0
#     for left in a:
#         right, total = (right + 1, total) if not left else (right, total + right)
#     return total if total < 1000000000000