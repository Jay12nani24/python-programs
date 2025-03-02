num = int(input("Enter a four-digit number: "))

if 1000 <= num <= 9999:
    d1 = num // 1000         
    d2 = (num // 100) % 10  
    d3 = (num // 10) % 10    
    d4 = num % 10            

    digit_sum = d1 + d2 + d3 + d4

    print(f"Sum of the digits: {digit_sum}")
else:
    print("Please enter a valid four-digit number!")
