n = int(input("Enter a number: "))  # Get number from user
sum = 0  # This will store the reversed number
x = n  # Make a copy of the original number

while x > 0:  
    digit = x % 10  # Get the last digit
    sum = sum * 10 + digit  # Add the digit to the reversed number
    x = x // 10  # Remove the last digit from x

# Compare the reversed number with the original number
if n == sum:  
    print("It is a palindrome")  
else:  
    print("It is not a palindrome")  
