# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def test():
    primesum = 2
    for testnum in range(3, 2000001, 2):
        for num in range(2, int(testnum**0.5)+1):
            if testnum % num == 0:
                break
        else:
            primesum += testnum
    print(primesum)
if __name__ == "__main__":
    test()