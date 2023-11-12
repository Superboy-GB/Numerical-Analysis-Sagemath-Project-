# Define a function to calculate the forward differences of a list of values
def forward_diff(values):
  n = len(values)
  diff = [[0 for i in range(n)] for j in range(n)]
  for i in range(n):
    diff[i][0] = values[i]
  for j in range(1, n):
    for i in range(n - j):
      diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
  return diff

# Define a function to calculate the factorial of a number
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1)

# Define a function to implement Newton's forward difference formula
def newton_forward(x, y, value):
  # x and y are lists of tabulated values
  # value is the point at which the interpolation is required
  n = len(x)
  h = x[1] - x[0] # Assume equal spacing
  a = (value - x[0]) / h # Calculate the value of a
  diff = forward_diff(y) # Generate the forward difference table
  result = y[0] # Initialize the result with the first term
  for i in range(1, n):
    term = diff[0][i] * a # Calculate the ith term
    for j in range(i):
      term *= (a - j) / factorial(i) # Multiply by the binomial coefficients
    result += term # Add the term to the result
  return result

# Example usage
x = [40, 50, 60, 70, 80]
y = [31, 73, 124, 159, 190]
value = 52
result = newton_forward(x, y, value)
rounded_result = round(result, 4)
print("The interpolated value at", value, "is", rounded_result)
