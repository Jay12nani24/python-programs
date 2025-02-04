str = input()  # Get input from the user

for i in range(len(str)):  # Loop through each character
    for j in range(i + 1, len(str) + 1):  # Loop to get all possible substrings
        print(str[i:j])  # Print the substring
