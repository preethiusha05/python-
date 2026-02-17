m1 = int(input("Enter marks for Subject 1: "))
m2 = int(input("Enter marks for Subject 2: "))
m3 = int(input("Enter marks for Subject 3: "))
print("Student Exam Result Program")

# Arithmetic Operators
total = m1 + m2 + m3
average = total / 3
percentage = (total / 300) * 100
print("\nTotal Marks =", total)
print("Average Marks =", average)
print("Percentage =", percentage)

# Comparison Operators
print("\nComparison Check")
print("m1 == m2 :", m1 == m2)
print("m1 != m2 :", m1 != m2)
print("m1 > m2 :", m1 > m2)
print("m1 < m2 :", m1 < m2)

# Logical Operators (Pass condition)
print("\nPass Condition")
if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Result : PASS")
else:
    print("Result : FAIL")

# Assignment Operators
bonus = total
bonus += 5     
print("\nAfter Grace Marks =", bonus)

# Identity Operators
x = [m1, m2, m3]
y = x
print("\nIdentity Check")
print("x is y :", x is y)
print("x is not y :", x is not y)

# Membership Operators
print("\nMembership Check")
check = int(input("Enter mark to check in list: "))
print("Mark in list :", check in x)
print("Mark not in list :", check not in x)

# Bitwise Operators (Using m1 and m2)
print("\nBitwise Operations")
print("m1 & m2 =", m1 & m2)
print("m1 | m2 =", m1 | m2)
print("m1 ^ m2 =", m1 ^ m2)
print("~m1 =", ~m1)
print("m1 << 1 =", m1 << 1)
print("m1 >> 1 =", m1 >> 1)

