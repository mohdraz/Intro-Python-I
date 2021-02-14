"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

# Output the second element: 4:
x = slice(1, 2, 1)
print(f"first output: {a[x][0]}")

# Output the second-to-last element: 9
y = a[slice(-2, -1, 1)]
print(f"second output is: {y[0]}")

# Output the last three elements in the array: [7, 9, 6]
# z = a[ slice(-3, len(a) , 1)]
# z = a[ slice(-3, len(a) , 1)]
z = a[-3:]
print(f"third output: {z}")


# Output the two middle elements in the array: [1, 7]
n = a[2:-2]
print(f"fourth output: {n}")

# Output every element except the first one: [4, 1, 7, 9, 6]
m = a[1:]
print(f"fifth output: {m} ")

# Output every element except the last one: [2, 4, 1, 7, 9]
b = a[0:-1]
print(f"sixth output: {b} ")

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
u = s[7:12]
print(f"seventh output: {u} ")
