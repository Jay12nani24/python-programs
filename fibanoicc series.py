num = int(input("Enter the number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci Sequence:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b  # Update values
