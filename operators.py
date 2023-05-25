# Arithmetic Operators
x = 10 + 5
y = 10 - 5
z = 10 * 5
w = 10 / 5
v = 10 // 3
m = 10 % 3
e = 2 ** 3

# Assignment Operators
a = 5
a += 2  # equivalent to: a = a + 2
b = 10
b -= 3  # equivalent to: b = b - 3
c = 3
c *= 4  # equivalent to: c = c * 4
d = 12
d /= 3  # equivalent to: d = d / 3
e = 15
e //= 4  # equivalent to: e = e // 4
f = 17
f %= 5  # equivalent to: f = f % 5
n = 10
n //= 3  # n = n // 3
m = 2
m **= 3  # m = m ** 3



# Comparison Operators
x = 10
y = 5
print(x > y)   # Greater than: True
print(x < y)   # Less than: False
print(x == y)  # Equal to: False
print(x != y)  # Not equal to: True
print(x >= y)  # Greater than or equal to: True
print(x <= y)  # Less than or equal to: False

# Logical Operators
p = True
q = False
print(p and q)  # Logical AND: False
print(p or q)   # Logical OR: True
print(not p)    # Logical NOT: False

# Bitwise Operators
x = 10  # Binary: 1010
y = 5   # Binary: 0101
print(x & y)  # Bitwise AND: 0 (Binary: 0000)
print(x | y)  # Bitwise OR: 15 (Binary: 1111)
print(x ^ y)  # Bitwise XOR: 15 (Binary: 1111)
print(~x)     # Bitwise NOT: -11 (Binary: 11111111111111111111111111110101)
print(x << 2) # Bitwise Left Shift: 40 (Binary: 101000)
print(x >> 2) # Bitwise Right Shift: 2 (Binary: 10)

# Membership Operators
lst = [1, 2, 3, 4, 5]
print(3 in lst)    # Check if 3 is in the list: True
print(6 not in lst)  # Check if 6 is not in the list: True

lst = [1, 2, 3, 4, 5]
is_member = 3 in lst  # True
is_not_member = 6 not in lst  # True


# Identity Operators
x = 10
y = 10
print(x is y)     # Check if x and y refer to the same object: True
print(x is not y) # Check if x and y refer to different objects: False


# String Operators
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
repeated_str = str1 * 3
is_member = "lo" in str1

# List Operators
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2
repeated_list = list1 * 3
is_member = 2 in list1

# Tuple Operators
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 3
is_member = 2 in tuple1

# Dictionary Operators
dict1 = {"a": 1, "b": 2, "c": 3}
is_key_member = "a" in dict1
is_value_member = 2 in dict1.values()

# Identity Operator
x = 10
y = 10
is_same_object = x is y
is_different_object = x is not y
