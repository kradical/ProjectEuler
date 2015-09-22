# Surprisingly there are only three numbers that can be written as the sum of
# fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth 
# powers of their digits.

def check_fifth_powersum(number):
    sum = 0
    numbercpy = number
    while number:
        sum += ( number % 10 ) ** 5
        number //= 10
    return sum == numbercpy

def main():
    ndx = 2
    fifth_power_sum = 0
    while ndx < 1000000:
        if check_fifth_powersum(ndx):
            print(ndx)
            fifth_power_sum += ndx
        ndx += 1
    print(fifth_power_sum)

if __name__ == '__main__':
    main()