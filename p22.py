# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
# containing over five-thousand first names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a name 
# score. For example, when the list is sorted into alphabetical order, COLIN, 
# which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
# COLIN would obtain a score of 938 * 53 = 49714. What is the total of all the 
# name scores in the file?

def main():
    with open('p22_names.txt', 'r') as fp:
        names = fp.read()
    result = [x.strip('"') for x in names.split(',')]
    result.sort()
    alpha_sum = 0
    for ndx, name in enumerate(result):
        print(ndx, name)
        alpha_sum += (ndx+1) * sum(ord(c) - 64 for c in name)
    print(alpha_sum)

if __name__ == '__main__':
    main()