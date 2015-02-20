# By listing the first six prime numbers: 2, 3, 5, 7, 11,
# and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?
# nth prime must be in range
# nln(n) + n(ln(ln(n))-1) < number < nln(n) + nln(ln(n))
#     lower_bound = int(search_prime*log(search_prime) + search_prime*(log(log(search_prime))-1))
#     upper_bound = int(search_prime*log(search_prime)+search_prime*log(log(search_prime)))


def is_prime(test_number):
    for i in range(2, int(test_number**0.5)+1):
        if test_number % i == 0:
            return False
    return True


def test():
    prime_ndx = 10001
    test_number = 3
    primes = [2]
    while True:
        if is_prime(test_number):
            primes.append(test_number)
        if len(primes) == prime_ndx:
            print(primes.pop())
            return
        test_number += 2

if __name__ == '__main__':
    test()