def solution(ar):
    stack = [None] * len(ar)
    size = 0
    blocks = 0

    for i in range(len(ar)):
        print(i, ar[i])

        while size > 0 and ar[i] < stack[size-1]:
            size -= 1
            print("while size", size)

        if size == 0 or ar[i] != stack[size-1]:
            blocks += 1
            stack[size] = ar[i]
            size += 1
            print("Block - {}, stack - {}, size - {}".format(blocks, stack, size))

    return blocks


a = [8, 8, 5, 7, 9, 8, 7, 4, 8]
print(solution(a))
