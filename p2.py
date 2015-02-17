# find the sum of the even terms of the fibonacci series up to 4 million
value = 0
number = 2

gr = ((1 + 5**.5) / 2)**3
while number < 4000000:
    value += number
    number = round(number*gr)
print(value)