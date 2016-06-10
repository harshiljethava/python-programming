str1="Int and boolean are Intergral data type "
print(str1)
x=-4.5
y=2000
s1='This is sample string to convert in int'
z=x+y
s2='20'
print("x: ",x," y: ",y)
print("addition z: ",z)
print("truncate divison : ",x//y)
print("absolute value: ",abs(x))
print("divmod(x,y) :",divmod(x,y))
print("binary : ",bin(y))
print("hex : ",hex(y))
print("octal :",oct(y))
#print("value of string : ",s1)
#print(int(s2,2))
print("bits requie to store y :",int.bit_length(y))
bs=int.bit_length(y)/8
print("byte require to store y :",int(bs))
