test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)]
def count_digits(tup):
    total = 0
    for num in tup:
        total += len(str(abs(num)))   
    return total

print("Sort Tuples by Total Digits")
result = sorted(test_list, key=lambda x: count_digits(x))
print("Sorted List:", result)
