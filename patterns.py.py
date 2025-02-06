# Right-Angled Triangle Pattern

rows = 5  # Number of rows in the pattern

for i in range(1, rows + 1):  #  number of rows (1 to 5)
    for j in range(1, i + 1):  #  number of stars (*) in each row
        print("*", end="")  # Print a star without a new line
    print("")  # Move to the next line


#Inverted Right-Angled Triangle

rows = 5
for i in range(rows, 0, -1):  # Loop starts from 5 and decreases to 1
    for j in range(i):  # Loop prints '*' i times in each row
        print("*", end="") 
    print("") 


#Pyramid Pattern

rows = 5 

for i in range(1, rows + 1):  # Loop from 1 to 5 (controls row count)
    print(" " * (rows - i) + "* " * i)  # Print spaces and stars


#Diamond Pattern

rows = 5

# First part - Upper pyramid
for i in range(1, rows + 1):  
    print(" " * (rows - i) + "* " * i)  

# Second part - Lower inverted pyramid
for i in range(rows - 1, 0, -1):  
    print(" " * (rows - i) + "* " * i)  



#Hollow Square

rows = 5  # Number of rows and columns

for i in range(rows):  # Loop to control rows (0 to 4)
    for j in range(rows):  # Loop to control columns (0 to 4)
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end=" ")  # Print star for borders
        else:
            print(" ", end=" ")  # Print space inside the square
    print("")  

    

#inverted diamond or countdown timer pattern

rows = 5  # Number of rows for the half pyramid

# Upper Inverted Pyramid
for i in range(rows, 0, -1):  # Starts from `rows` down to 1
    print(" " * (rows - i) + "* " * i)

# Lower Regular Pyramid
for i in range(2, rows + 1):  # Starts from 2 up to `rows`
    print(" " * (rows - i) + "* " * i)