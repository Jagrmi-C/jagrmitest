# from operator import xor

# __________________________
# |    |    | AND| OR | XOR|
# __________________________
# |  0 |  0 |  0 |  0 | 0  |
# __________________________
# |  1 |  0 |  0 |  1 | 1  |
# __________________________
# |  0 |  1 |  0 |  1 | 1  |
# __________________________
# |  1 |  1 |  1 |  1 | 0  |
# __________________________

n1 = 38
n2 = 53

# bit OR
bit_or = n1 | n2
print(bin(n1)[2:])
print(bin(n2)[2:])

print(bin(bit_or)[2:])
print(f"The result for the bit operation OR for numbers {n1} and {n2} is {bit_or}, binary - {bin(bit_or)}")
# bit AND
bit_and = n1 & n2
print(bin(n1)[2:])
print(bin(n2)[2:])

print(bin(bit_and)[2:])
print(f"The result for the bit operation AND for numbers {n1} and {n2} is {bit_and}, binary - {bin(bit_and)}")
# bit XOR
n3 = 138
n4 = 43
bit_xor = n3 ^ n4
print(bin(n3)[2:])
print(bin(n4)[2:])

print(bin(bit_xor)[2:])
print(f"The result for the bit operation XOR for numbers {n3} and {n4} is {bit_xor}, binary - {bin(bit_xor)}")

# NOT
bit_not = ~ n1
print(bin(n1)[2:])
print(bin(bit_not).split('b')[1])
print(f"The result for the bit operation NOT for numbers {n1}  is {bit_not}")
