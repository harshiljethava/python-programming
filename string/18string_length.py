def string_length(string):
    if len(string) < 3:
        return string
    else:
        new_string = string[:3]
        return new_string

string = input("enter string : ")
print("\nresult : ", string_length(string))
