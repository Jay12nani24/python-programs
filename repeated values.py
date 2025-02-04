n = input() 
found = False  # A flag to check if a repeated value is found

#  each character in the input string starting from index 1
for j in range(1, len(n)):  
    # Check all previous characters before the current character at index j
    for i in range(0, j):  
        if n[i] == n[j]:  # If a duplicate character is found
            print(n[j])  # Print the repeated character
            print(f"Repeated value : {n[j]} at index {j}")  # Show the repeated character and its index
            found = True  # Mark that we found a repeated character
            break  # Exit the inner loop (we don't need to check further for this character

# If no repeated character was found, print this
if not found:  
    print("No repeated value")  
