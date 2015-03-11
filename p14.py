# The following iterative sequence is defined
# for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting
# with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet
# (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


def main():
    longest_sequence_length = 0
    for x in range(500000, 1000000):
        current_sequence_length = 0
        collatz_number = x
        while collatz_number != 1:
            current_sequence_length += 1
            if collatz_number % 2 == 0:
                collatz_number /= 2
            else:
                collatz_number = 3 * collatz_number + 1
        if current_sequence_length > longest_sequence_length:
            longest_sequence_length = current_sequence_length
            print("{}, {}".format(x, longest_sequence_length))

if __name__ == '__main__':
    main()