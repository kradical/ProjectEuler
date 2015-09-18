# Starting with the number 1 and moving to the right in a clockwise direction a
# 5 by 5 spiral is formed as follows:
# 43  44 45 46 47 48 49
# 42  21 22 23 24 25 26
# 41  20  7  8  9 10 27
# 40  19  6  1  2 11 28
# 39  18  5  4  3 12 29
# 38  17 16 15 14 13 30
# 37  36 35 34 33 32 31 
# It can be verified that the sum of the numbers on the diagonals is 101.
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?

def spiralcount(num):
    ndx = 1
    step = 2
    cntr = 0
    diagonal_sum = 1
    while ndx < num**2:
        ndx += step
        diagonal_sum += ndx
        
        cntr += 1
        if cntr % 4 == 0:
            step += 2
    return diagonal_sum
    

def main():
    print(spiralcount(1001))
    
if __name__ == '__main__':
    main()