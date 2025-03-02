from datetime import date

today = date.today()

birth_day = int(input("Enter your birth day (DD): "))
birth_month = int(input("Enter your birth month (MM): "))
birth_year = int(input("Enter your birth year (YYYY): "))

age_years = today.year - birth_year
age_months = today.month - birth_month
age_days = today.day - birth_day

if age_months < 0 or (age_months == 0 and age_days < 0):
    age_years -= 1 

print(f"\nYour age is: {age_years} years")
