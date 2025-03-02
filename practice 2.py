tam= float(input("Enter marks for tam : "))
mat  = float(input("Enter marks for  mat : "))
sci = float(input("Enter marks for sci : "))
eng = float(input("Enter marks for eng : "))
soc = float(input("Enter marks for  soc : "))

total_max_marks = 5 * 100 

aggregate = tam + mat + sci + eng + soc 
percentage = (aggregate / total_max_marks) * 100

print("\nResults:")
print(f"Aggregate Marks: {aggregate}")
print(f"Percentage: {percentage:.2f}%")
