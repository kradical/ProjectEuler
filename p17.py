# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand)
# inclusive were written out in words, how many
# letters would be used?
# NOTE: Do not count spaces or hyphens. For example,
# 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters.
# The use of "and" when writing out numbers is in compliance
# with British usage.
letter_to_length = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4}
tens_letter_to_length = {'0': 0, '2': 6, '3': 6, '4': 5, '5': 5, '6': 5, '7': 7, '8': 6, '9': 6}
ten_to_twenty = {'0': 3, '1': 6, '2': 6, '3': 8, '4': 8, '5': 7, '6': 7, '7': 9, '8': 8, '9': 8}


def letter_count(number):
    total = 0
    if number[0] != '0': # hundred place
        total += 7 # add for the word hundred
        if number[1] != '0' or number[2] != '0':
            total += 3 # add for the word and
    total += letter_to_length[number[0]]
    if number[1] == '1': # tens place and ones place for 10-19
        total += ten_to_twenty[number[2]]
    else:
        total += letter_to_length[number[2]] # tens place
        total += tens_letter_to_length[number[1]] # ones place
    print('{}, {}'.format(number, total))
    return total


def main():
    total = 0
    for x in range(1, 1000):
        number = str(x)
        while len(number) < 3:
            number = '0' + number
        total += letter_count(number)
    total += 11 #for one thousand just so the loop only deals with 3 digit numbers
    print(total)

if __name__ == '__main__':
    main()