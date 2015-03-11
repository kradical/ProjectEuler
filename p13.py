# Work out the first 10 digits of the sum
# of 100 fifty digit numbers
import sys


def main():
    file = open(sys.argv[1], 'r')
    total = 0
    for line in file:
        total += int(line)
    print(str(total)[0:10])

if __name__ == '__main__':
    main()