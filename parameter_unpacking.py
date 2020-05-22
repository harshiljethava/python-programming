import math
def parafun(*args):
    cot=0
    for a in args:
        cot+=a
    return cot
"""
n=int(input("how many number you want to enter"))
print("please enter",n," numbers")
t1=[]
for i in range(0,n):
    val=0
    print("enter no for",i+1," element")

    val=int(input())
    t1.insert(i,val)
    i+=1
"""
print("passing (1,3,4,6,4):",parafun(1,3,4,6,4))

print("passing (134452637,7453,74353754,47446,43633):",parafun(134452637,7453,74353754,47446,43633))

print("passing (445,46,54):",parafun(445,46,54))

print("passing (54.0):",parafun(54.0))

print("Moral : with parameter unpacking it is possible to make fun which has dynamic parameter passing facility.")


a=3;b=3
def paramfun1(*,woo="paramfun1()`s woo"):
    print("""\nparamfun1(*,woo="paramfun1()`s woo")""")
    po=math.pow(a,b)
    print("paramfun1():",po,"woo :",woo)

paramfun1()

p=3;q=4
def paramfun2(p,q,woo="paramfun2()`s woo"):
    print("""\nparamfun2(p,q,woo="paramfun2()`s woo")""")
    po=math.pow(p,q)
    print("paramfun2():",po,"woo :",woo)

paramfun2(p,q)
print("Moral: by putting '*' in starting of fun arguments dont require any other parameter for passing and keyword arguments are allowed.")

