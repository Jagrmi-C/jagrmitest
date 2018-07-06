def fib(n):
    sequence_list = []
    current_number = 0
    next_number = 1
    for i in range(n + 1):
        sequence_list.append(current_number)
        current_number = next_number
        if i > 0:
            # next = sequence_list[i] + current
            next_number = sequence_list[i] + current_number
        else:
            next_number = 1
    return sequence_list[n]


print(fib(10))
print(fib(40))
print(fib(1))
print(fib(0))
