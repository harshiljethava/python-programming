#input output

x1=input("enter number 1: ")
#int(x)
x2=input("enter number 2: ")
print("Type of x1: ",type(x1) ," and x2: ",type(x2))
x=int(x1)+int(x2)
print("Checking type with 'int()'")
print("Type of x1: ",type(int(x1)) ," and x2: ",type(int(x2)))
print("Using 'int()' for addition : ",x)
x=x1+x2
print("Addition without 'int()': ",x)
print("\n>>>Without using 'int()' with 'input()'")
y1=input("Enter number for y1: ")
print("Value of y1: ",y1)
print("Type of y1: ",type(y1)," <<==")
print("\n>>>With using 'int()' with 'input()' // Eg: int(input())")
y1=int(input("Enter number for y1: "))
print("Value of y1: ",y1)
print("Type of y1: ",type(y1)," <<==")

