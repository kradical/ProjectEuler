# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number
# 600851475143 ?
import heapq
from functools import partial
import timeit


def test():
    prime_factors = [-317584931803]
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
                # print(current_factor)
                return
            current_divisor += 1

if __name__ == "__main__":
    test()
    # times = timeit.Timer(partial(test)).repeat(3, 1000)
    # print(min(times)/1000)