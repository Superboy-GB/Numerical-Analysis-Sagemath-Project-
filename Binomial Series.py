X = 1  # Coefficient of X
Y = 3.0  # Coefficient of Y
exp = 4  # Value of n
terms = 5  # Number of terms to be obtained

# The rest of your code (factorial, solve) remains unchanged

def factorial(n):
    return 1 if (n == 0 or n == 1) else n * factorial(n - 1)

def solve(a, b, ex, var):
    j = -1
    h = ex
    while j < var:
        j = j + 1
        aExp = ex - j
        sumt = pow(a, aExp)
        sumy = pow(b, j)
        ansOne = (sumt * sumy) / factorial(j)
        g = ex - (j - 1)
        h = h * g
        if j < 1:
            h = 1
        answer = h * ansOne
        appAns = round(answer, 4)
        print(appAns)

solve(X, Y, exp, terms)
