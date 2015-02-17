# A palindromic number reads the same both ways.
# The largest palindrome made from the product
# of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product
# of two 3-digit numbers.


def main():
    current_greatest = 0
    for number1 in range(100, 1000):
        for number2 in range(100, 1000):
            new_palindrome = number1*number2
            if str(new_palindrome) == str(new_palindrome)[::-1]:
                if new_palindrome > current_greatest:
                    current_greatest = new_palindrome
    print(current_greatest)


if __name__ == "__main__":
    main()
