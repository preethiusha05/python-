m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

result = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)
    result.append(row)

print("Generated 2D Array:")
print(result)
