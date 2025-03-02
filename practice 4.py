notes_100 = int(input("Enter the number of ₹100 notes: "))
notes_500 = int(input("Enter the number of ₹500 notes: "))
notes_1000 = int(input("Enter the number of ₹1000 notes: "))

total_amount = (notes_100 * 100) + (notes_500 * 500) + (notes_1000 * 1000)

print(f"\nTotal amount withdrawn: ₹{total_amount}")
