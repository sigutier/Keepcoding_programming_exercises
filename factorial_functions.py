# Factorial functions
def inception(n):
    if n <= 0:
        return 1
    else:
        return n * inception(n - 1)

def inception_while(n):
    if n <= 0:
        return 1
    else:
        factorial = 1
        while n > 0:
            factorial *= n
            n -= 1
    return factorial

def inception_for(n):
    if n <= 0:
        return 1
    else:
        factorial = 1
        for i in range (1, n + 1):
            factorial = factorial * i
    return factorial
