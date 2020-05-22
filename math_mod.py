import math,decimal
m1=3.00000000001
m2=4

print("m1:",m1,"|| m2 :",m2)
print("valu of m1:",m1)
print("Using ceil() fun with m1: ",math.ceil(m1)," // return smallest integer greater than equal to value entered")
m1=-3.9
print("New value of m1 :",m1)
print("Using ceil() with m1 : ",math.ceil(m1))
print("Type of m1 : ",type(m1))
print("Type of math.ceil(m1): ",type(math.ceil(m1)))

m3=-5.0
m4=9
print("m3 :",m3," || m4: ",m4)
print("Using copysign() with m3 and m4 copysign(m3,m4) : ",math.copysign(m3,m4))
print("Moral : copysign(m3,m4) copy sign of m4 to m3")

m5=12.
print("\nm5: ",m5)
print("Type of m5: ",type(m5))
print("Using degress() with m5: ",math.degrees(m5))
print("Moral : Convert float m5 from radians to degrees // Python takes 12 as redians value and convert to into degrees")

m6=1
print("\nm6: ",m6)
print("Using exp() with m6: ",math.exp(m6))
print("Type of math.exp(): ",type(math.exp(m6)))
print("Moral: exp() return value of <<e raise to x>> ")

m7= math.e
print("\nvalue of constant e: ",math.e)
print("value of constant e with decimal.Decimal(): ",decimal.Decimal(math.e))

m8=-7.7
print("\nm8: ",m8)
print("Using fabs(), absolute value of m8: ",math.fabs(m8))

m9= 16.3
print("\nvalue of m9: ",m9)
print("Using floor() with m9: ",math.floor(m9))
print("Changing value from 16.3 to -16.3")
m9=-16.3
print("Using floor() with m9: ",math.floor(m9))
print("Moral: floor() return largest interger less than or equal to value entered.")

m10=5
m11=2
print("\nm10: ",m10,"|| m11: ",m11)
print("Using fmod() with m10 ,m11 > fmod(m10,m11): ",math.fmod(m10,m11))
print("Moral: produce remainder(modulus) of m10 to m11 // better than % in float")


m12=7
print("\nm12: ",m12)
print("Using frexp() with m12: ",math.frexp(m12))
print("Moral: return 2 tuple ,first contains mentissa as a 'float' and exponent as an 'int' // m12= m* 2 raise to e , \n\tm12= 0.875*2 raise to 3 ")


m13=1000000000000000000000000000000000000000000000000000000000000000000000000000000.0
print("\nm13: ",m13)
print("Type of m13:",type(m13))
print("m13 has infinite value:  ",math.isinf(m13))
print("Moral: isinf() returns 'True' if entered float value is infinite otherwise return 'False' ")

m14=120
print("\nm14: ",m14)
print("Type of m14: ",type(m14))
print("Using isnan() with m14: ",math.isnan(m14))
m14=120.
print("Change value of m14 from 120 to 120. ")
print("Type of m14: ",type(m14))
print("Using isnan() with m14: ",math.isnan(m14))


print("\nconstant pi:",math.pi)
print("\nconstant pi using decimal.Decimal():",decimal.Decimal(math.pi))

m15=20
print("\nm15: ",m15)
print("Using factorial() ,value of m15: ",math.factorial(m15))
print("Type of math.factorial(m15): ",type(math.factorial(m15)))

print("\n\n===<<WANT TO SEE MAGIC ,ENTER NUMBER GREATER THAN 1000 FOR FACTORIAL AND SEE POWER OF PYTHON !!!>>===")

m16=input("\nEnter number greater than 1000 for factorial")
print("\nfactorial of ",m16," is: ",math.factorial(decimal.Decimal(m16)))

print("input() has string return type ,so first of all entered value should be converted in 'int' .\n =)This can be done in 2 way \n1>> m16=int(m16)\n2>> math.factorial(int(m16))")

print("\n\n<<If you want to see magic then re-run program  .\nTHIS TIME PLEASE CHECK CPU PERCENTAGE IN  TASK MANAGER ;)>>")
