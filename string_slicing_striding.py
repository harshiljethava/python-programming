str1="Life is long process of learning."
print("Our sample string str1:",str1)
print("\nstr1[0]:",str1[0])
print("str1[1]:",str1[1])
print("str1[2]:",str1[2])
print("str1[3]:",str1[3])
print("str1[4]:",str1[4])
print("str1[5]:",str1[5])

print("Moral: with indexing we have printed single character of string 'str1' one by one,remember positive indexing starts from '0'.")

print("\nstr1[-10]:",str1[-10])
print("str1[-11]:",str1[-11])
print("str1[-12]:",str1[-12])
print("str1[-13]:",str1[-13])
print("str1[-14]:",str1[-14])
print("str1[-15]:",str1[-15])

print("Moral: with negative indexing we haved printed single character of string 'str1' from position -10 to -15 (indexing strarted from right to left side)\
,remember negative indexing strarts from -1.")

print("\nstr1[-10]==str1[23]:",str1[-10])
print("str1[-11]==str1[22]:",str1[22])

print("str1[-12]==str1[21]:",str1[21])
print("Moral:negative indexing and positive indexing can be use with each other ,just to care about right index position !")


print("\nstr1[0:33]:",str1[0:33])
print("str1[0:10]:",str1[0:10])
print("str1[1:5]:",str1[1:5])
print("str1[2:10:2]:",str1[2:10:2])
print("str1[2:10:3]:",str1[2:10:3])
print("str1[:10:2]:",str1[:10:2])
print("str1[::2]:",str1[::2])
print("str1[5::3]:",str1[5::3])
print("str1[::]:",str1[::])

print("Moral:with slicing ,possible to print string 'str1' in desire substring here 3 parameters \
available [starting point : ending point : step point] ||this is slicing with positive indexing.")
print("\nstr1[0:33]:",str1[0:33])
print("str1[-32:-25]:",str1[-32:-25])
print("str1[-12:-10]:",str1[-12:-10])
print("str1[-33:-20]:",str1[-33:-20])
print("str1[-33:-20:2]:",str1[-33:-20:2])
print("str1[-33:-10:-2]:",str1[-33:-10:-2])
print("Moral:slicing can be done with negative indexing too but here care should be taken while using negative stepping.")
print("\nstr1[0:33]:",str1[0:33])
print("""str1[0:7]+str1[8:12]+"adding 'but beautiful' string":""",str1[0:7]+str1[8:12]+" BUT BEAUTIFUL")
print("Moral:it is possbile to concate sliced substring with new string.")

print("str1[::-1]:",str1[::-1])
print("str1[::-2]:",str1[::-2])
print("str1[-30::-1]:",str1[-30::-1])
print("str1[-30:-10:-1]:",str1[-30:-10:-1])
print("str1[::2]:",str1[::2])
print("str1[::-2]:",str1[::-2])
print("Moral:using negative indexing in step parameter ,called as striding.Its just like reverse of string.")
print("""\n" ".join(str1):"""," ".join(str1))
print(""""*".join(str1):""","*".join(str1))
print(""""^".join(str1[0:10]):""","^".join(str1[0:10]))
print("Moral: .join() take a sequence as arugment as and joins them togather int single string. ")
print("\nreversed(str1):",reversed(str1))

str2= "*"
str3="#"
print("\nstr2:",str2,"|| str3:",str3)
print("str2*10:",str2*10)
print("str3*20:",str3*20)
str4="This is string 'str4'."
str5="'This is'"
print("\nstr4:",str4)
print("str5:",str5)
print("str5 in str4:",str5 in str4)
str6="'This is not'"
print("str6:",str6)
print("str6 in str4:",str6 in str4)
print("Moral:using memebership operator 'in' with string ,gives 'True' if left-hand string is a substring of right-hand string.")
print("")
for i in range(0,len(str1)):
    print("str1[",i,"]:" ,str1[i])
print("See string in new way")

for i in range(1,len(str1)):
    print("str1[",-i,"]:",str1[-i])
print("str1[0]:",str1[0])
