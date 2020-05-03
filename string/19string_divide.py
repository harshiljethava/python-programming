def string_split(string):
    char = input("enter the character to split string : ")
    new_string = string.split(char)
    print("new_string : ",new_string)
    return print("first : %s last : %s"%(new_string[0],new_string[-1]))

string = input("enter string : ")
call = string_split(string)