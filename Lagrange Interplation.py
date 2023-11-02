from sympy import symbols, simplify

# We Define the Lagrange interpolation function
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

# Example usage: Determine the Polynomial P_2(x) = a_0 + a_1x + a_2x2 whose graph passes through the points (1, 4), (2, 0) and (3, 12).
x_values = [0, 1, 3]
y_values = [0, 1, 0]

interpolation_polynomial = lagrange_interpolation(x_values, y_values)
expanded_polynomial = expand(interpolation_polynomial)
print(f"Hence, the Polynomial is {expanded_polynomial}")

# Evaluate the polynomial at a specific x value

# Function to evaluate the Lagrange interpolation polynomial at a specific x value
#def evaluate_interpolation(x_value, interpolation_polynomial, x_symbol):
    #return interpolation_polynomial.subs(x_symbol, x_value)

#x_value_to_evaluate = 1
#result = evaluate_interpolation(x_value_to_evaluate, interpolation_polynomial, x)
#print(f"The value of the polynomial at x = {x_value_to_evaluate} is {result}")
