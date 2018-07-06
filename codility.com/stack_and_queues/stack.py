
stack = [9, 2, 3, 1, 4]
size = 0


def push(x):
    global size
    stack[size] = x
    size += 1


def pop():
    global size
    size -= 1
    return stack[size]


push(5)
push(6)
push(1)

print(stack)

print(pop())
print(stack)
print(pop())
print(stack)
