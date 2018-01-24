from timeit import timeit


def is_palindrome(number):
    return str(number) == str(number)[::-1]

MIN = 10000
MAX = 100000


def largest():
    max_number = 0
    for i in range(MAX-1, MIN-1, -1):
        for j in range(MAX-1, i - 1, -1):
            product = i * j
            if product > max_number and is_palindrome(product) :
                max_number = product
    return max_number

print(timeit('largest()', 'from __main__ import largest', number = 1))
print(largest())
