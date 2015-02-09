sum1 = 0
for x in range(1000):
    print(x)
    if (x % 3 == 0) or (x % 5 == 0):
        sum1 += x
print(sum1)