# Starting in the top left corner of a 2×2 grid, and
# only being able to move to the right and
# down, there are exactly 6 routes to the bottom
# right corner.
# How many such routes are there through a 20×20 grid?
# will be the 21st central binomial coefficient
#(2*21)!/21!

import math


def main():
    number = math.factorial(40)/(math.factorial(20)**2)
    lattice_path = [[1] for x in range(21)]
    for x in range(20):
        lattice_path[0].append(1)
    for i in range(1, 21):
        for j in range(1, 21):
            lattice_path[i].append(lattice_path[i][j-1] + lattice_path[i-1][j])
    for row in lattice_path:
        print(row)
    print(number)

if __name__ == '__main__':
    main()