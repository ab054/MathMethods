from numpy.linalg import inv

# Matrix A
x = [[11, 4, 2],
     [5, 6, 3],
     [4, 5, 8]]

print("Inverted of A: ")
result = inv(x)
for r in result:
    print(r)
