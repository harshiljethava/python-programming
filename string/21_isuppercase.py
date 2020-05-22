def to_uppercase(string):
    count = 0
    for letter in string[:3]:
        if letter.isupper() is True:
            count += 1
    if count >= 2 :
        return string.upper()
    return string
string = input("enter string : ")
print("\nresult  : ",to_uppercase(string))