n = int(input("Enter the N-th number: "))  

count = 0  # Number of primes found
num = 1    # Start checking from number 2 onwards

while count < n:  # Keep searching until we find the N-th prime
    num += 1  # Move to the next number
    is_prime = True  # Assume the number is prime

    # Check if the number is divisible by any number from 2 to sqrt(num)
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:  # If divisible, it's NOT a prime number
            is_prime = False  # Mark as not prime
            break  # Stop checking further

    if is_prime:  # If the number is still prime
        count += 1  # Increase the prime count

# Once the loop ends, print the N-th prime number found
print(f"The {n}-th prime number is: {num}")
