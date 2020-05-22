ncerti=["compTIA N+","CCNA","CCNP","CCIE"]
scerti=["MCSA","MCSE","RHCSA"]
hcerti=["CEH","CHFI"]
print("\nNetworking Certificates:",ncerti)
print("Server Certificates:",scerti)
print("Security Certificates:",hcerti)
print("\nI want to pass {0[2]} and {0[3]} certificate".format(ncerti))
print("I want to pass {0[2]} and {0[3]} certificate.format(ncerti)")
print("\nI want to get detailed knowledge about {0[0]} and {0[1]}".format(ncerti))
print("I want to get detailed knowledge about {0[0]} and {0[1]}.format(ncerti)")
print("\nI want to pass {0[1]},{0[2]},{0[3]} and {1[0]},{1[1]} o_O".format(ncerti,scerti))
print("I want to pass {0[1]},{0[2]},{0[3]} and {1[0]},{1[1]} o_O.format(ncerti,scerti)")
print("\nBecause of lack of time I cant have {0[3]},{1[1]},{2[0]}".format(ncerti,scerti,hcerti))
print("Because of lack of time I cant have {0[3]},{1[1]},{2[0]}.format(ncerti,scerti,hcerti)")
#print("\nMoral: fomat() method can be used with list by providing index position of element in list ,which wanted to display in string.")

price=35000
certi="CEH"
str1="cost of Certificate <{certi}> may be around <{price}> ".format(**locals())
print("\nstr1 ,using **locals() inside format():",str1)
print("Moral:**locals() can be useful when to use local variable that are currently in scope are available from built-in locals() method.\
** known as mapping unpacking opeartor.")
