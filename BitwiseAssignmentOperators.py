# 1. Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print(f"a + b = {a + b}")   # Addition
print(f"a - b = {a - b}")   # Subtraction
print(f"a * b = {a * b}")   # Multiplication
print(f"a / b = {a / b}")   # Division (float)
print(f"a // b = {a // b}") # Floor Division
print(f"a % b = {a % b}")   # Modulus
print(f"a ** b = {a ** b}") # Exponent
print()

# 2. Relational / Comparison Operators
print("Comparison Operators:")
print(f"a == b : {a == b}")
print(f"a != b : {a != b}")
print(f"a > b  : {a > b}")
print(f"a < b  : {a < b}")
print(f"a >= b : {a >= b}")
print(f"a <= b : {a <= b}")
print()

# 3. Logical Operators
x = True
y = False
print("Logical Operators:")
print(f"x and y : {x and y}")
print(f"x or y  : {x or y}")
print(f"not x   : {not x}")
print()




m = 6   # (binary 110)
n = 3   # (binary 011)
print("Bitwise Operators:")
print(f"m & n = {m & n}")   # AND
print(f"m | n = {m | n}")   # OR
print(f"m ^ n = {m ^ n}")   # XOR
print(f"~m = {~m}")         # NOT
print(f"m << 1 = {m << 1}") # Left shift
print(f"m >> 1 = {m >> 1}") # Right shift



# Bitwise Assignment Operators

x = 5   # 0101 (binary)
print("Initial x:", x)

x |= 10   # x = x | 10 → 0101 | 1010 = 1111 (15)
print("x |= 10:", x)

x &= 7    # x = x & 7 → 1111 & 0111 = 0111 (7)
print("x &= 7 :", x)

x ^= 3    # x = x ^ 3 → 0111 ^ 0011 = 0100 (4)
print("x ^= 3 :", x)

x <<= 2   # x = x << 2 → 0100 << 2 = 10000 (16)
print("x <<= 2:", x)

x >>= 1   # x = x >> 1 → 10000 >> 1 = 1000 (8)
print("x >>= 1:", x)
