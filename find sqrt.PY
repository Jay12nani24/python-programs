# Ask the user to enter a number and store it as a decimal number
num = float(input("Enter a number: "))

# Find the square root of the number by raising it to the power of 0.5
square_root = num ** 0.5

# Show the number and its square root, keeping 3 decimal places for both
print("The square root of %0.3f is %0.3f" % (num, square_root))
