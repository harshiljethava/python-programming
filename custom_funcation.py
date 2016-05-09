print("Python provide 4 type of fun \
\n1.global \n2.local \n3.lamba fun\n4.methods")
i,j,k=1,2,3
def ad(i,j,k):
    return i+j+k
print("sum:",ad(i,j,k))
print("return type of ad(i,j,k) fun:",type(ad(i,j,k)))
def check_type():
    return
"""
print("return type of check_type fun:",check_type())
print("Moral :Every fun in python has return value it may be any type including \
tuple,collection and set.Default return of any fun is None.")
"""
s1="This is sample string"
def lens1(s1):
    for i in s1:
        print(i)
    return "just printed characters of s1"
lens1(s1)
print("Whats statement of return :",lens1(s1))

def passfun(a,b):
    print("a:",a)
    print("Type of a:",type(a))
    print("b:",b)
    print("Type of b:",type(b))
    if type(a)==float or type(b)==int :
        print("a,b both has diff data type")
    elif type(a)==int and type(b)==int:
        print("b,c both has same type but 'int'")
    elif type(a)==float and type(b)==float:
        print("b,c both has same type but 'int'")
    else:
        print("stil cant find ,Guess !!")
a=float(input("enter <float> no"))
b=int(input("enter <int> no"))

passfun(a,b)

def defpass(str1,key="!!!!!!"):
    if len(str1)>10:
        print("string with key:",str1+" "+key)
    else:
        print("string without key:",str1)

str1=input("Enter your string")

defpass(str1)

print("Moral:It is possible to make fun arguments with default value.")
print("Given Default values are assigned when def is executing not when fun is called .")
