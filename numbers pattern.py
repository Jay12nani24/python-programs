rows = 5  # Number of rows
for i in range(1, rows + 1):  # Loop through each row
    for j in range(1, i + 1):  # Print numbers from 1 to i
        print(j, end="")  # Print without newline                          
    print("")  # Move to the next line after each row
    
 #output  
1                                                                            
12                                                                         
123                                                                          
1234                                                                         
12345    

# in line 4 if we change i instead of j 
#output
1
22
333
4444
55555