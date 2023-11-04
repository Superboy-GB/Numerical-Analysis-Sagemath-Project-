def simpsons_rule(func, a, b, n):
    """
    Compute the numerical integral of a function using Simpson's Rule.
    
    Parameters:
    - func: The function to be integrated.
    - a: The lower bound of the integral.
    - b: The upper bound of the integral.
    - n: The number of subintervals. n must be an even number.
    
    Returns:
    - The approximate integral value.
    """
    if n % 2 != 0:
        raise ValueError("n must be an even number for Simpson's Rule.")
    
    h = (b - a) / n
    integral = func(a) + func(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral

# Example usage:
def f(x):
    return 2/x**(1/2)  # Replace this with your own function

a = 1
b = 3
n = 4  # Number of subintervals

result = simpsons_rule(f, a, b, n)

print(result)
