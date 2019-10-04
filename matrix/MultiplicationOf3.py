from numpy.linalg import multi_dot

# Matrix A
x = [[11, 4, 2],
     [5, 6, 3],
     [4, 5, 8]]

# Matrix B
y = [[4, 5, 5],
     [6, 7, 3],
     [4, 5, 9]]

# Matrix C
z = [[4, 5, 5],
     [6, 7, 3],
     [4, 5, 9]]

multiplicationOf3 = multi_dot([x, y, z])

print("Matrix A * B * C = Z: ")
for r in multiplicationOf3:
    print(r)
