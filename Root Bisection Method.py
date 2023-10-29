# Define the function for which you want to find the root
def f(x):
    return 5*(x**2) + 11*x - 17

# Bisection method
def bisection_method(f, a, b, tol, max_iter):
    if f(a) * f(b) >= 0:
        print("Bisection method may not converge as f(a) and f(b) have the same sign.")
        return None

    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Bisection method did not converge within the maximum number of iterations.")
    return None

# Set the initial interval [a, b], tolerance (tol), and maximum number of iterations
a = 0
b = 3
tolerance = 1e-6
max_iterations = 100

# Call the bisection method function
root = bisection_method(f, a, b, tolerance, max_iterations)

#To round up to a 3 significant values as given
result = round(root, 3)

if root is not None:
    print(f"The approximate root found is {result}")
