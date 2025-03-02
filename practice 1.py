base_price = float(input("Enter the base price of the product: ₹"))
cgst_rate = 9 / 100
sgst_rate = 11 / 100
cgst_amount = base_price * cgst_rate
sgst_amount = base_price * sgst_rate
total_price = base_price + cgst_amount + sgst_amount
print(f"Base Price: ₹{base_price:.2f}")
print(f"CGST (9%): ₹{cgst_amount:.2f}")
print(f"SGST (11%): ₹{sgst_amount:.2f}")
print(f"Total Price to Pay: ₹{total_price:.2f}")