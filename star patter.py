rows = 5  # Define the number of rows for the pattern

# Outer loop to control the rows (from 1 to 5)
for i in range(1, rows + 1):
    
    # Inner loop to control the number of '*' in each row
    for j in range(1, i + 1):  # Loop runs 'i' times to print '*' in each row
        print("*", end="")  # Print '*' without moving to the next line
    print("")  # After printing all '*' in the current row, move to the next line
