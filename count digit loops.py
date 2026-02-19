text = input("Enter a string: ")
letters = 0
digits = 0
spaces = 0
others = 0
for ch in text:
    if ch.isalpha():
        if ch.isupper():
            letters += 1
        elif ch.islower():
            letters += 1
        else:
            pass
    elif ch.isdigit():
        digits += 1  
    elif ch.isspace():
        spaces += 1
        continue
    else:
        others += 1
print("\nResults:")
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)
print("Other Characters:", others)
