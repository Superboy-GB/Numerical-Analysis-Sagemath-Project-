x = var('x')
f(x) = (x**3) - 3
df = diff(f, x)
NewtonIt(x) = x - f(x) / df(x)

x_initial = 2  # Initial guess
tolerance = 1e-6  # Tolerance for convergence

iteration = 1
while True:
    x_new = NewtonIt(x_initial)
    print(f"Iteration {iteration}: x{iteration} = {x_new.n(digits=6)}")
    
    if abs(x_new - x_initial) < tolerance:
        print(f"Hence, {x_new.n(digits=6)} is the root of {f(x)}")
        break
    
    x_initial = x_new
    iteration += 1


