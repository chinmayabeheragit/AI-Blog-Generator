# Define a jagged array
arr = [[1], [2, 3], [4, 5, 6]]

# Access elements
for row in arr:
    for val in row:
        print(val, end=" ")
    print()
# Output:
# 1
# 2 3
# 4 5 6
