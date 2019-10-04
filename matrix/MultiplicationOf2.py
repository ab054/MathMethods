# Program to multiply two matrices using nested loops

# Matrix A
x = [[11, 4, 2],
     [5, 6, 3],
     [4, 5, 8]]
# Matrix B
y = [[4, 5, 5, 7],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]
# result Matrix is C:
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

# iterate through rows of x
for i in range(len(x)):
    # iterate through columns of y
    for j in range(len(y[0])):
        # iterate through rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

print("Matrix  A: ")
print(x)

print("Matrix  B: ")
print(x)

print("Matrix A * B = C: ")
for r in result:
    print(r)
