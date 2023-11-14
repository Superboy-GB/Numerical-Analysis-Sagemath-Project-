# Define the function
def f(x):
    return x^2 - 3*x + 1

# Define the iterative formula
def g(x):
    return (x^2 + 1)*(1/3)

# Initial guess
x0 = 0
# List to store the iterations
iterations = [x0]

# Perform the iterations
for i in range(100):
    x1 = g(x0)
    iterations.append(x1)
    # Check for convergence
    if abs(x1 - x0) < 1e-6:
        break
    x0 = x1

print("The root is {:.3f}".format(x1.n()))

