import decimal,sys,cmath
f1=4.5e-5
print(f1)
print(type(f1))
f2=7e-4
print("value of f2:",f2)
f3=66E+10
print("value of f3:",f3)
f4=5.
print("value of f4:",f4)
f5=-2.5e+4
print("value of f5:",f5)
f6=1.0e+100
print("value of f6:",f6)
print("type of f6: ",type(f6))
f7=1.e+1000
print("value of f7: ",f7,""" // real value of f7 = 1.0e+1000\nMoral :float has limited percision (only 2 digit) level comapared to int and decimal  """)

f71=decimal.Decimal(1e+1000)
print("value of f71 using decimal.Decimal(): ",f71)
print("""\nThis output provide more clear and sensible information compared to float.
      \nDecimal holds 28 decimal places accuarcy level !.\nBut has lower processing capability compared to float """)

f8=8.
i1=9
print("\nf8 :",f8,"i1: ",i1)
print("Type of f8:",type(f8),"\nType of i1:",type(i1))
fi=f8+i1
print("addition of f8 and i1: ",fi)
print("Type of addition fi: ",type(fi))
print("\nMoral : arithematic calclultion of 'int' and 'float' produces <<float>> \n\t=>same as 'float' and 'complex' produces <<complex>>\n\t=>In this program used decimal.Decimal() has highest precision level so it can be used with only <<decimal>>")

print("\n\nFloat Information : ",sys.float_info)

c1=8+7j
print("\nc1: ",c1)
print("Type of c1: ",type(c1))
print("Real element: ",c1.real)
print("Imagianry element:",c1.imag)
print("To change sign of imaginary element, use conjugate():",c1.conjugate())
print("\nUse 'cmath' module with complex number ,\nwhich provide many trigonometric and logarithmic funn,specified to complex number")
