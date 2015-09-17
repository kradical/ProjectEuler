# A unit fraction contains 1 in the numerator. The decimal representation of 
# the unit fractions with denominators 2 to 10 are given:
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be 
# seen that 1/7 has a 6-digit recurring cycle. Find the value of d < 1000 for
# which 1/d contains the longest recurring cycle in its decimal fraction part.
# see: http://mathworld.wolfram.com/DecimalExpansion.html

def main():
    max = (0,0)
    for x in range(10, 1000):
        prev = []
        power = 0
        while True:
            value = 10**power % x
            if value in prev:
                break
            prev.append(10**power % x)
            power += 1      
        s = prev.index(10**power % x) 
        t = power - s    
        if t > max[1]:
            max = x, t
    print(max[0], "has the longest cycle of numbers < 1000. It is", max[1], "decimal places long.")     

if __name__ == '__main__':
    main()