#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Solving integration using trapezoidal rule
fx = input("Enter f(x): ")
n = int(input("No of sub-intervals(stripe): "))
a = eval(input("Enter lower limit: "))
b = eval(input("Enter upper linit: "))


h = (b - a)/n
xis = [a + i*h for i in range(n+1)]

def eval_poly(poly, val):
    xs = [x.strip().replace('^', '**') for x in poly.split('+')]
    return sum([eval(n.replace('x', str(val))) for n in xs])

def integral_solution():
    xis_left = xis.copy()
    xis_left.remove(a)
    xis_left.remove(b)

    xis_sum = 0
    for i in range(len(xis_left)):
        xis_sum = 2*(eval_poly(fx, xis_left[i])) + xis_sum

    sol = (h/2)*(eval_poly(fx, xis[0]) + eval_poly(fx, xis[n]) + xis_sum)

    print("\nThe solution to the integral f(x) is ", round(sol, 2))

integral_solution()

import matplotlib.pyplot as plt
xis
y = [eval_poly(fx, x) for x in xis]
plt.plot(xis, y);
plt.title('Graph of f(x)');
plt.xlabel('x-axis (xis)');
plt.ylabel('y-axis (f(xis))');


# In[ ]:





# In[ ]:




