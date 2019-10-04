from numpy.linalg import eigh

# Matrix A
x = [[11, 4, 2],
     [5, 6, 3],
     [4, 5, 8]]

print("Return the eigenvalues and eigenvectors of a symmetric matrix: ")
result = eigh(x)
for r in result:
    print(r)
