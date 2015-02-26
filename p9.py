# A Pythagorean triplet is a set of three
# natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet
# for which a + b + c = 1000.
# Find the product abc.


def test():
    for a in range(1, 333):
        for b in range(1000-a):
            c = 1000-b-a
            if a**2 + b**2 == c**2:
                print(a*b*c)
                return

if __name__ == "__main__":
    test()