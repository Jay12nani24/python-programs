
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x, y = a, b
while x != y:
    if x > y:
        x = x - y
    else:
        y = y - x
gcd = x

lcm = (a * b) // gcd

print(f"GCD of {a} and {b} is {gcd}")

print(f"LCM of {a} and {b} is {lcm}")  