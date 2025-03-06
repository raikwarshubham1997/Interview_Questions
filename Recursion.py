# factorial n!=n*(n-1)*(n-2)

def Factorial(n):
    if n == 0 or n == 1:    # Base condition
        return 1

    else:
        return n * Factorial(n-1)  # Recursive call