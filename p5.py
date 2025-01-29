n = int(input("Enter a number: "))  # User inputs a number
sum = 0  # Variable to store the sum of cubes of digits
x = n  # Copy the original number to 'x' for processing

while (x > 0):  # Loop runs as long as 'x' is greater than 0
    digit = x % 10  # Extract the last digit of 'x'
    sum = sum + digit * digit * digit  # Add the cube of the digit to 'sum'
    x = x // 10  # Remove the last digit from 'x' (integer division)

# After the loop, compare the calculated sum with the original number
if (n == sum):  
    print("It is an Armstrong number") 
else:
    print("It is not an Armstrong number") 