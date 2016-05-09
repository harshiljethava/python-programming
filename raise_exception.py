print("raise with exception")
"""i=0;j=1
print("i:",i,"|| j:",j)
try:
    k=j/i  
except Exception  as ze:
    print("error")

finally:
    print("finally")
"""
class DeviceError(Exception) :pass
        
try:
    print("\nInside Try block")
    i=input("Enter your required device")
    if i=="router" or i=="switch":
        print("we have your required device ")
        print("You asked for:",i)
    else:
        raise DeviceError("No device found")

finally:
    print("\nFinally block ")
    print("completed")
