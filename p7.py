str1 = input("Enter string 1: ")  # Get first string
str2 = input("Enter string 2: ")  # Get second string

if len(str1) == len(str2):  # Check if both strings have the same length
    sorted_str1 = sorted(str1)  # Sort the characters of str1
    sorted_str2 = sorted(str2)  # Sort the characters of str2
    
    if sorted_str1 == sorted_str2:  # Compare sorted versions
        print("It is an anagram")  
    else:
        print("It is not an anagram")  
else:
    print("It is not an anagram")  
