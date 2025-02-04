a = int(input("Enter a number for a: "))  # User inputs a number for 'a'
b = int(input("Enter a number for b: "))  # User inputs a number for 'b'

print("Before swapping:", (a, b))  # Display original values of 'a' and 'b'

# Swapping logic without using a third variable
a = a + b  # Step 1: Add both numbers and store the sum in 'a'
b = a - b  # Step 2: Subtract 'b' from the new 'a' to get the original 'a' in 'b'
a = a - b  # Step 3: Subtract new 'b' from 'a' to get the original 'b' in 'a'

print("After swapping:", (a, b))  # Display swapped values
