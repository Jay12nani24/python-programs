# Ask the user to enter a year and store it as a number
year = int(input("Enter a year: "))

# Check if the year is divisible by 400 (these years are always leap years)
if (year % 400 == 0):
    print(" %i is a leap year" % (year))

# If not divisible by 400, check if the year is divisible by 4 but NOT by 100
elif (year % 4 == 0) and (year % 100 != 0):
    print(" %i is a leap year" % (year))

# If neither of the above conditions is true, it's not a leap year
else:
    print(" %i is not a leap year" % (year))
