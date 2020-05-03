def char_exchange(string):
    print(string[-1])
    print(string[1:-1])
    print(string[:1])
    return string[-1:] + string[1:-1] + string[:1]


string = str(input("Enter string : "))
print("\n result :", char_exchange(string))
