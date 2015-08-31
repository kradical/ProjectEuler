# Counting Sundays
# You are given the following information, but you may prefer to do some 
# research for yourself.
#     1 Jan 1900 was a Monday.
#     Thirty days has September,
#     April, June and November.
#     All the rest have thirty-one,
#     Saving February alone,
#     Which has twenty-eight, rain or shine.
#     And on leap years, twenty-nine.
#     A leap year occurs on any year evenly divisible by 4, but not on a 
#     century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def main():
    daylist = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    day = 2
    first_sundays = 0
    for year in range(1901, 2001):
    	first_sundays += 1 if day%7 == 0 else 0 # JAN
    	day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # FEB
    	day += 29 if year % 4 == 0 and year % 100 != 0 else 28
        first_sundays += 1 if day%7 == 0 else 0 # MAR
        day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # APR
    	day += 30
    	first_sundays += 1 if day%7 == 0 else 0 # MAY
    	day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # JUN
    	day += 30
    	first_sundays += 1 if day%7 == 0 else 0 # JUL
    	day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # AUG
    	day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # SEP
    	day += 30
    	first_sundays += 1 if day%7 == 0 else 0 # OCT
    	day += 31
    	first_sundays += 1 if day%7 == 0 else 0 # NOV
    	day += 30
    	first_sundays += 1 if day%7 == 0 else 0 # DEC
    	day += 31
    print(first_sundays)

if __name__ == '__main__':
	main()