from sympy import symbols, simplify

# Define the Lagrange interpolation function
def lagrange_interpolation(x_values, y_values):
    n = len(x_values)
    x = symbols('x')
    result = 0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return simplify(result)

# Example usage:
x_values = [1, 2, 3]
y_values = [4, 0, 12]

interpolation_polynomial = lagrange_interpolation(x_values, y_values)
expanded_polynomial = expand(interpolation_polynomial)
print(expanded_polynomial)