#format() method of string
#str0="When you are student of life then you dont require to depent only books for learning."
str1="Life is beautiful."
print("str1:",str1)
print("""str1 with format()>>\
\n{0}Life is beatiful{1}.format("My",",in problems too"):""","{0}Life is beautiful{1}".format("My ",",in problems too"))
str2="my date of birth is"
print("\nstr2:",str2)
print("""str2 with format()>> \nstr2+'{0}'.format("13 feb")'""",str2+'{0}'.format(" 13 feb"))
print("""\n"{0}{1}{2}".format("This is"," combination"," of 3 strings")>>\n""","{0}{1}{2}".format("This is"," combination"," of 3 strings"))

str3="THREE"
print("\nstr3:",str3)
str4="'{0}{1}{2}'"
str5="FIVE"
str6="SIX"
print("str4:",str4);print("str5:",str5);print("str6:",str6)
print("""str4.format("one ","two ",str3)>>""",str4.format("one "," two ",str3))
print("""str4.format(str5,str6,str3) >> """,str4.format(str5,str6,str3))
print("Moral: format() method provie flexible mechanism to customise string format.")

print("\nI am {profession} but first of all <{quality}>".format(profession="Engineer",quality="a Humble Human."))
print("I am <{what}> person who like to code at <{0}> AM".format("1:30",what=" Geek"))
#print("{my} tunned {age} this year".format(my="he",age=21))
print("Moral: with format() ,field name can be used to provide predefined value to string \
// Eg> Engineer, a Humble person || Geek ,1:30 all are just value which passed to aproperiate field name.")
