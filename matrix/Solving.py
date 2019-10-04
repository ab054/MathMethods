from numpy.linalg import solve

# Matrix A
x = [[3, 1],
     [1, 2]]

b = [9, 8]
print("Solve the system of equations: ")
result = solve(x, b)
for r in result:
    print(r)
