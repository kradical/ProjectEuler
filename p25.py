# The Fibonacci sequence is defined by the recurrence relation:
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# What is the index of the first term in the Fibonacci sequence to contain 
# 1000 digits?

def fib(x):
    prev = 0
    cur = 1
    for y in range(x):
        temp = cur
        cur = cur + prev
        prev = temp
    return cur
    
def main():
    prev = 0
    cur = 1
    for x in range(1, 10000):
        cur = fib(x)
        if len(str(cur)) == 1000:
            print(x+1, "is the first index of a 1000 digit fibonacci number")
            break

if __name__ == '__main__':
    main()