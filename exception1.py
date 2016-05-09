print("exception with data type")
t1=("first",2,"three",4.0)
print("t1:",t1)
try:
    print("\ninside try block")
    if type(t1[1])==int: 
        print("value of t1[1]:",t1[1])
        print("type of value t1[1]:",type(t1[1]))
        print("yes !t1[1] has int data type")
    else:
        raise TypeError 
except TypeError as e:
    print("\nERROR: ",e)
else:
    print("")
finally:
    print("\nFinally block")
    for i in t1:
        print(i,":",type(i))
    print("completed")

l1=[12,343,4,45,"nice",(1,2),["aa","bb"]]
print("\nlist l1:",l1)
c=1
for i in l1:
    print(c,".",i,":",type(i))
    c+=1
try:
    print("\nInside try block")
    dt=input("enter your choice for data type")
    if(dt=='str'):
        dt=""
    elif(dt=='int'):
        dt=0
    elif(dt=='tuple'):
        dt=()
    elif(dt=='list'):
        dt=[]
    elif(dt=='dict'):
        dt={}
    else:
        print("invalid choice")
    print(dt)
    
    print(type(dt))
    if (type(l1[0]) or type(l1[1]))==type(dt):
        print("l1[0] and l1[1] has same data type")
    else:
        raise TypeError
except TypeError as te:
    print("\nERROR:",te)
    print("They have not same data type !!")
else:
    print("May be they have 'int' data type")
finally:
    print("\nFinally block")
    print("completed")
