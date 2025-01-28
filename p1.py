# Ask the user to enter a number
n = int(input("Enter a number: "))

# Check if the number is less than or equal to 1
if n <= 1:
    # If the number is 1 or less, it's not a prime number
    print("Not prime")
else:
    # Check all numbers starting from 2 up to (but not including) n
    for i in range(2, n):
        # If n is divisible by any number in this range
        if n % i == 0:
            # It's not a prime number
            print(n, "is not prime")
            break  # Stop checking further
    else:
        # If no divisors are found, it's a prime number
        print(n, "is prime")
