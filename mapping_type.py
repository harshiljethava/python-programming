"""print("Python 3.1 has 3 type of mapping type or dictionary")
print("1> dict \n2>collections.defaultdict\n3>collections.OrderedDict*")

print("works well with ==,!= but not with (<,>,>=)")
"""
d1=dict(id=1,name="ram",cont=123456)
print("d1:",d1)
print("Type of d1:",type(d1))
d2={"add":"ahmedabad","brach":"it","semster":4}
print("d2:",d2)
print("Type d2['add']",type(d2["add"]))
print("""Type d2["brach"]:""",type(d2["brach"]))
print("""Typed2["semster"]:""",type(d2["semster"]))
print("d2['add']:",d2['add'])
print("d2['brach']:",d2['brach'])
print("d2['semster']:",d2['semster'])

d3=dict(zip(("key","type","value","amount"),(120,"normal",2.5,("rupee",1000.0))))
print("d3:",d3)

print("d3['key']:",d3['key'])
d4=dict([("key",1020),("pass","123abc"),('account',"vvip")])
print("d4:",d4)
d5={"domain":"org","price":125000,"validity":"lifetime"}
print("d5:",d5)

d6={"root":"super_user",700:"standard",-20:None,"demo_tuple":(1,2,11,1),0:25}
print("d6",d6)
d6['root']=100000
print("after assign 100000 to 'root'")
print(d6)
del d6[-20]
print("delete -20")
print(d6)
print(len(d6))

for i in d6.items():
    print(i[0],":",i[1])

for key,value in d6.items():
    print(key,":",value)
i=0
for value in d6.values():
    print("value",i,":",value);
    i+=1
j=0
for k in d6.keys():
    print("key",j,":",k)
    print("Type of key",j,":",type(k))
    j+=1

