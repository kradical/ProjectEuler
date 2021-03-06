# The sequence of triangle numbers is
# generated by adding the natural numbers.
# So the 7th triangle number would be
# 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven
# triangle numbers:
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle
# number to have over five divisors.
# What is the value of the first triangle
# number to have over five hundred divisors?
import heapq
from collections import Counter


def primefactorization(number_to_factorize):
    prime_factors = [-number_to_factorize]
    while prime_factors:
        current_divisor = 2
        current_factor = -heapq.heappop(prime_factors)
        sqrt_current_factor = int(current_factor**0.5)
        while True:
            if current_factor % current_divisor == 0:
                heapq.heappush(prime_factors, int(-current_divisor))
                heapq.heappush(prime_factors, int(-(current_factor/current_divisor)))
                break
            elif current_divisor == sqrt_current_factor+1:
                heapq.heappush(prime_factors, int(-current_factor))
                divisors = 1
                for key, value in Counter(prime_factors).items():
                    divisors *= (value + 1)
                return divisors
            current_divisor += 1


def test():
    counter = 1
    while True:
        triangle_number = int(counter*(counter+1)/2)
        number_of_divisors = primefactorization(triangle_number)
        if number_of_divisors >= 500:
            print(triangle_number)
            break
        counter += 1

if __name__ == '__main__':
    test()