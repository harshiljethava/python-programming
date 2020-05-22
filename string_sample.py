#example of string
"""This program provide sufficient information about string\n
python except raws string and format method of string"""
str1='''this is triple quote string'''
print("1 ",str1)
str2="what\'s plan for tomorrow ?"
print("2 ",str2)
str3='This is third string in single quote'
print("3 ",str3)
str4="""This is fourth string \nwith new line """
print("4 ",str4)
str5='''This is fifth string \t\twith tab '''
print("5 ",str5)
str6="""This is sixth string with "double string" inside"""+str2+""" outside"""
print("6 ",str6)
str7='This is seventh string """with triple string inside """'
print("7 ",str7)
str8='This is eightth string ""with double string inside""'
print("8 ",str8)
str9='This is nineth string with """triple""" and ""double string inside""'
print("9 ",str9)
str10="This is tenth string with single quote of 'it\'s' name "
print("10 ",str10)
str11="This is eleventh string with \n""""triple"""" string"
print("11 ",str11)
print("String Escapes")
print("\\t > ASCII tab")
print("\\n > ASCII linefeed")
print("this is test \f work")
print("\\f > ASCII formfeed")
print("this is test of \a")
print("\\a > ASCII bell")
print("this is test of \b")
print("\\b > ASCII backaspace")
print("this is test of \r")
print("\\r > ASCII carriage return")
print("this is test of \v")
print("\\v > vertical tab")
print("\n\n\t <<Built-in string method intro (Total 35 methods !!!)>>")
s="life is process of learning"
print("Our test string s : ",s)
print("1> s.capitalize():",str.capitalize(s))
print("2> s.center(string,padding): ",s.center(30))
print("3> s.count(substring,start,end): ",s.count("i"),"// count occurance of 'i' in string 's'")
print("4> s.encode: ",s.encode())
print("5> s.endswith(): <<",s.endswith("l"),">>")
s="life is process of learningl"
print("New modified string s: ",s)
print("5.1> s.endswith(): <<",s.endswith("$$$$"),">>")
s="life is process of learning"
print("6> s.expandtabs(size): ",s.expandtabs())
print("7> s.find('f',3,len(s)): ",s.find('f',3,len(s)))
print("8> s.index('f',3,len(s)): ",s.index('f',3,len(s)))
print("9> s.rindex('f',0,len(s)): ",s.rindex('f',0,len(s)))
print("10> s.isalnum(): ",s.isalnum()," // return 'True' if every \
character in 's' alphanumeric")
print("11> s.isalpha(): ",s.isalpha()," // return 'True' if every \
character in 's' alphabetic")

print("12> s.isdecimal(): ",s.isdecimal()," // return 'True' if \
every character in 's' is Unicode base 10 decimal")

print("13> s.isdigit(): ",s.isdigit()," // return 'True' if every \
character in 's' alphanumeric")

print("14> s.isidentifier(): ",s.isidentifier()," // return 'True' if  \
's' is valid identifier ")
print("15> s.islower(): ",s.islower()," // return 'True' if every \
character in 's' is lower case")
print("16> s.isnumeric(): ",s.isnumeric()," // return 'True' if every\
character in 's' is  numeric")
print("17> s.isspace(): ",s.isspace()," // return 'True' if every character in 's' is space")

#print("5> s.decode(): ",s.decode())
#str12=

#s1="""__"""
#s2='''__'''
#s3="_"
#s4='_'
#s5="""_'__'_"""
#s6="""_"__"_"""
#s7="_'__'_"
#s8="_"""__"""_"
