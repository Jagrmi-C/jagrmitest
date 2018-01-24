def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True

print(isprime(33211))
print(isprime(11))


print(isprime(99923))
print(isprime(87541))
