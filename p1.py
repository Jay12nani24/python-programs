# Accept user input as an integer
n = int(input("Enter a number: "))

# Check if the input number is less than or equal to 1
if n <= 1:
    # Numbers less than or equal to 1 are not prime
    print("Not prime")
else:
    # Loop through all numbers from 2 up to (but not including) n
    for i in range(2, n):
        # Check if n is divisible by i (i.e., remainder is 0)
        if n % i == 0:
            # If divisible, n is not a prime number
            print(n, "is not prime")
            break  # Exit the loop since we've found a divisor
    else:
        # The 'else' block of the loop is executed if the loop is not broken
        # If no divisors are found, the number is prime
        print(n, "is prime")
