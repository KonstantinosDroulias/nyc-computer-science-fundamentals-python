print("Leap Year Checker")
year = int(input('Type year: '))

if year % 4 != 0 and year % 100 != 0 and year % 400 != 0:
    print(f'Year {year} is not a leap year')
else:
    print (f'Year {year} is a leap year')