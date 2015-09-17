# A permutation is an ordered arrangement of objects. For example, 3124 is one 
# possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
# are listed numerically or alphabetically, we call it lexicographic order. The
# lexicographic permutations of 0, 1 and 2 are:
# 012   021   102   120   201   210
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
# http://www.nayuki.io/page/next-lexicographical-permutation-algorithm

import math

def scan_for_pivot(digitlist):
    prev = -math.inf
    for ndx, digit in enumerate(reversed(digitlist)):
        if digit < prev:
            return len(digitlist) - 1 - ndx
        prev = digit
    return None         
   
def scan_for_swap(pivot, digitlist):
    for ndx, digit in enumerate(reversed(digitlist)):
        if digit > digitlist[pivot]:
            return len(digitlist) - 1 - ndx
    
def main():
    digits = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    for x in range(0, 999999):
        pivot = scan_for_pivot(digits)
        if pivot == None:
            break
        swap = scan_for_swap(pivot, digits)
        digits[pivot], digits[swap] = digits[swap], digits[pivot]
        digits[pivot+1:] = reversed(digits[pivot+1:])
    print(''.join(str(x) for x in digits), "is the millionth lexicographic configuration")
    
if __name__ == '__main__':
    main()