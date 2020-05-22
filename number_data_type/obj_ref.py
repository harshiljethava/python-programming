#object reference

x=1
y='2'
z=3.0
print("x: ",x," y: "+y," z: ",z)
print("Type of x : ",type(x))
print("Type of y : ",type(y))
print("Type of z : ",type(z))
x=1,

print("length: ",len(x))
print(x)
print("Type of X : ",type(x))
print(" >> example of dynamically typed language")
y='2',
print("length: ",len(y))
print(y)
print("Type of Y : ",type(y))
z=3.0,
print("length: ",len(z))
print(z)
print("Type of Z : ",type(z))

x=11,
y=11,

print("x: ",x," y: ",y)
print("x is y : ",x is y," // comparing object reference ")
print("x == y : ",x==y," // comparing value of x and y" )
x=y
print("AFTER x=y\n")
print("x is y : ",x is y,"// after assigning y to x both object reference is same ")
print("x == y : ",x==y)
print("\n MORAL >> use 'is','is not','none' when comparing object reference and use '==','!=' when comparing values of object refernce")

z=3.0
print("\nvalue of z :",z)
print("0 < z < 10 : ",0<z<10)
print("0 < z <= 3 : ",0<z<=3)
print("0 < z < 3 : ",0<z<3)
print("0 > z > 3 : ",0>z>3)
z1=3
z2=3.0
print("Z1: ",z1," Z2: ",z2)
print("Type of Z1: ",type(z1),"\nType of Z2: ",type(z2))
print("Z1 is Z2: ",z1 is z2)
print("Z1 == Z2: <<",z1==z2,">>")
print("\n1>> Now we are changing value of z2 to 3.000001")
z2=3.000001
print("Z1: ",z1," Z2: ",z2)
print("Type of Z1: ",type(z1),"\nType of Z2: ",type(z2))
print("Z1 is Z2: ",z1 is 2)
print("Z1 == Z2: <<",z1==z2,">>")

print("\n2>> Now we are changing value of z2 to <<3.000000000000000000000001>>")
z2=3.000000000000000000000001
print("Z1: ",z1," Z2: ",z2)
print("Type of Z1: ",type(z1),"\nType of Z2: ",type(z2))
print("Z1 is Z2: ",z1 is 2)
print("Z1 == Z2: <<",z1==z2,">>")
x1=1
print("\n\nvalue of X1: ",x1)
x1=2
print("New value of X1: ",x1)
print("X1==2 : ",x1==2)
print("X1 is 2 : ",x1 is 2)
