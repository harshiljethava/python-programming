import collections,decimal
dd1=collections.defaultdict(str)
print(dd1)
print("dd1['xyz']",dd1['xyz'])
print(dd1)
dd1['xyz']=159
print(dd1)
print("dd1[250]:",dd1[250])
dd1[250]="address_vlaue"
print(dd1)
print("dd1[100]:",dd1[100])
print(dd1)
dd1[100]=decimal.Decimal(23.364584856151348541646854)
print(dd1)
print(type(dd1[100]))
