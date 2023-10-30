# Define the mathematical function or expression you want to plot
f(x) = # Your expression

# Create a plot of the function in the range a to b
p = plot(f, (x, a, b), title='Simple Plot', legend_label= (# Your function in the next hyphens)'',
color='blue')

# Show the plot
p.show()

         # Define the mathematical function or expression you want to plot
f(x) = (15-3*x)/3 - (7*x-14)/3

# Create a plot of the function in the range a to b
p = plot(f, (x, -1, 10), title='Simple Plot', legend_label= 'Graph of (15-3*x)/3 - (7*x-14)/3', color='blue')

p += point((2, 3),(5, 7), color='red', size=30)
# Show the plot
p.show()
