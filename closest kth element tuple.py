test_tup = (10, 22, 28, 29, 30, 40)
K = 3
target = test_tup[K]
closest_pair = ()
min_diff = float('inf')
for i in range(len(test_tup)):
    for j in range(i + 1, len(test_tup)):

        pair_sum = test_tup[i] + test_tup[j]
        diff = abs(pair_sum - target)

        if diff < min_diff:
            min_diff = diff
            closest_pair = (test_tup[i], test_tup[j])
print("Closest Pair to Kth index element")
print("Target value:", target)
print("Closest pair:", closest_pair)
