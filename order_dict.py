import collections
od1=collections.OrderedDict([('a',1),('b',2),('c',3)])
print(od1)
od2=collections.OrderedDict()
od2[1]="planning"
od2[2]="creating"
od2[3]="developing"
od2[4]="testing"
print(od2)

od3=collections.OrderedDict(zip(("key","name","passport","amount",12),(1200,"rajiv","fasfasf3242352",5000)))
print("od3:",od3)
print("Type of od3:",type(od3))
