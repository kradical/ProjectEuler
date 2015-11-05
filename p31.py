# In England the currency is made up of pound, £, and pence, p, and there are
# eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

def count_combs(money, coins):
    if money == 0:
        return 1
    elif len(coins) == 0 or money < 0:
        return 0
    else:
        return count_combs(money-coins[0], coins) + count_combs(money, coins[1:len(coins)])

def main():
    denominations = [200, 100, 50, 20, 10, 5, 1]
    amount = 200    
    print(count_combs(amount, denominations))
                                
    
if __name__ == '__main__':
    main()