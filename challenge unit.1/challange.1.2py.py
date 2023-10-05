def isleapyear (year):
    if (yaer % 4==0 and year % 100!=0)or year %400==0:
        return True
    else:
        return False
year =int(input("Enter a yera:"))
if isleapyear(yaer):
    print("{}is a leap year.".format(year))
else:
    print('{} is not a leap year,'.format(year))
