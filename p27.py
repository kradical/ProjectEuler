# Euler discovered the remarkable quadratic formula:
# n² + n + 41
# It turns out that the formula will produce 40 primes for the consecutive 
# values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 
# is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is clearly 
# divisible by 41.

# The incredible formula  n² − 79n + 1601 was discovered, which produces 
# 80 primes for the consecutive values n = 0 to 79. The product of the
# coefficients, −79 and 1601, is −126479.

# Considering quadratics of the form:
# n² + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |−4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression 
# that produces the maximum number of primes for consecutive values of n, 
# starting with n = 0.

def eulerpoly(a, b, x):
    return x**2+a*x+b

def isprime(num):
    if num % 2 == 0:
        return False
    
    if num < 0:
        return False
    
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True
                
    
def main():
    max_prime_streak = (0, 0, 0)
    for a in range(-1000, 1000):
       for b in range(-1000, 1000):
            x = 0
            while isprime(eulerpoly(a, b, x)):
                x += 1
            if x > max_prime_streak[2]:
                max_prime_streak = (a, b, x)
    print(max_prime_streak[0] * max_prime_streak[1], "is the product of coefficients", max_prime_streak[0], max_prime_streak[1])

if __name__ == '__main__':
    main()