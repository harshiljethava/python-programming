#tuple
import collections
certi="ccna","ccnp","ccie",200,200,300,400
scerti="mcsa",
print("scerti>> 1 tuple using comma :",scerti)
print("Sample tuple:",certi)

print("CEH not as tuple:",certi[:2],"CEH",certi[2:])
ncerti=certi[:2]+("CEH",)+certi[2:]
print("ncerti>> CEH as tuple:",ncerti)

print("\nType of CEH:",type(("CEH",)))
print("Type of ncerti:",type(ncerti))
print("Moral: be careful while using 1 tuple ,and checking type of it.!!!")
print("certi.count('ccna'):",certi.count("ccna"))
print("certi.count('200'):",certi.count(200))
print("certi.index('CCNA') // 'CCNA' is not element of certi tuple so it throws 'ValueError'.")
#print("certi.index('CCNA'):",certi.index("CCNA"))
print("certi.index('ccna'):",certi.index("ccna"))

t1=1,2,"three"
t2=4,5,"six"
print("t1:",t1)
print("t2:",t2)
print("cont t1+t2:",t1+t2)
print("cont t1[0:2]+t2[0:2]:",t1[0:2]+t2[0:2:])
print("cont t1[-1]+t2[-1]:",t1[-1]+t2[-1])

print("\nconcate t1[-1]+t2[-3]:",t1[-1]+str(t2[-3]))

print("\nstepping in tuple [::2]:",certi[::2])
print("negative stepping [-1::-2]:",certi[-1::-2])
(a,b)=("one",2)
print("a:",a," b:",b)
print("type ofa:",type(a))
print("type of (a,b):",type((a,b)))
cisco=("ccna","ccnp","ccie")
redhat=("rhcsa","rhce","rhca")
microsoft=("mcitp","mcsa","mcse")
h_certi=(cisco,redhat,microsoft)
print("Nested Tuple:",h_certi)
print("h_certi[0][1][2]:",h_certi[0][1][2]," #print 'n' from 'ccnp'")
print("h_certi[0][2][2]:",h_certi[0][2][2]," #print 'i' from 'mcitp'")
print("h_certi[1][2]:",h_certi[1][2])
print("Type of h_certi[1][2]",type(h_certi[1][2]))


print("\n\nNamed Tuple")
Salary=collections.namedtuple("Salary","weekly monthly yearly")
print("Salary:",Salary)
Work=collections.namedtuple("Work","hour")
print("Work:",Work)
salary=[]
salary.append(Salary(100,1000,10000))
print(salary)
work=[]
work.append(Work(10))
print(work)
total=0
for i in salary:
    for j in work:
        total+=i.weekly*j.hour
        print(total)
