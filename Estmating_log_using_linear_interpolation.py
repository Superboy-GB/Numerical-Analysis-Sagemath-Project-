
# Define the two points for linear interpolation
point_1 = [1, 0]
point_2 = [6, 1.7918]

# Perform linear interpolation
def linear_interpolation(point_1, point_2, x):
    x_0, y_0 = point_1
    x_1, y_1 = point_2
    interpolated_value = ((x - x_0) * (y_1 - y_0) / (x_1 - x_0)) + y_0
    return interpolated_value

# Estimate log2 using linear interpolation
x_value = 2  # The x-value for which you want to estimate log2
estimated_log = linear_interpolation(point_1, point_2, x_value)

print(f"Estimated log({x_value}) is approximately {estimated_log:.5f}")
