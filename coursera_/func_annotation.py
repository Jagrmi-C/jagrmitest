# Using annotation stile
def add(x: int, y: int) -> int:
    return x + y


print(add(10, 11))
print(add('still', 'works'))


def foo(*args, **kwargs):
    pass


print(foo(1, 2, 3, a="b"))


answer = list(map(lambda x: str(x), range(10)))
print(answer)


a = list(zip(filter(bool, range(3)),
             [x for x in range(3) if x]))

print(a)