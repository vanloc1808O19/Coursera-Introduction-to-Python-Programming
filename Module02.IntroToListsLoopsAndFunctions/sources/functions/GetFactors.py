import math

def getFactors(x):
    """Return a list of factors of a given number x."""
    
    factors = []

    for i in range(1, int(math.sqrt(x)) + 1, 1):
        if x % i == 0:
            factors.append(int(i))
            factors.append(int(x / i))
    
    factors.sort()
    
    return factors

x = int(input("Enter an integer: "))
ans = getFactors(x)
print(ans)