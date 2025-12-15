# Recursive function to find factorial
def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)


# Recursive function to find power
def power(base, exp):
    if exp == 0:             # base case
        return 1
    return base * power(base, exp - 1)


# Testing the functions
print("Factorial of 5:", factorial(5))
print("Power (2^4):", power(2, 4))
