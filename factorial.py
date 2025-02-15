
num = int(input("Enter a Number : "))  # Initialize the factorial variable to 1
factorial = 1  # Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i
print(f"The factorial of {num} is {factorial}")
