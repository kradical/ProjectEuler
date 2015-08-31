# n! means n * (n - 1) * ... * 3 * 2 * 1
# For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
# and the sum of the digits in 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
# Find the sum of the digits in the number 100!

def factorial(num):
	if num == 1:
		return 1
	else:
	    return factorial(num-1)*num

def main():
	number = factorial(100)
	result = [int(i) for i in str(number)]
	print(sum(result))

if __name__ == '__main__':
	main()