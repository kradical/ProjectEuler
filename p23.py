# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of 28 
# would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number. A 
# number n is called deficient if the sum of its proper divisors is less than n 
# and it is called abundant if this sum exceeds n. As 12 is the smallest abundant
# number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the
# sum of two abundant numbers is 24. By mathematical analysis, it can be shown 
# that all integers greater than 28123 can be written as the sum of two abundant 
# numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as 
# the sum of two abundant numbers is less than this limit Find the sum of all the
# positive integers which cannot be written as the sum of two abundant numbers.

def isabundant(num):
    divisors = {1}
    for x in range(2, int(num**0.5) + 1):
        if num%x == 0:
            divisors.add(x)
            divisors.add(num//x)
    if sum(divisors) > num:
        return True
    return False

def main():
    abundantset = set([])
    finalset = {x for x in range(20162)}
    for x in range(12, 20162):
        if isabundant(x):
            abundantset.add(x)
            for y in abundantset:
                finalset.discard(y+x)
            
    print(sum(finalset))
    
if __name__ == '__main__':
    main()