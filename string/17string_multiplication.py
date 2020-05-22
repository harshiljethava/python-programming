def string_copy(string):
    value = string[-2:]
    n = int(input("enter n : "))
    value = value * n
    return value

string = input("enter string : ")
print("\nresult : ",string_copy(string))