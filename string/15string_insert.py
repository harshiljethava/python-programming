<<<<<<< HEAD
def string_insert(string):
    middle = int((len(string)/2))
    word = input("\n enter new word to add : ")
    new_string = string[:middle] + word + string[middle:]
    return new_string

string = input("\n enter string : ")
=======
def string_insert(string):
    middle = int((len(string)/2))
    word = input("\n enter new word to add : ")
    new_string = string[:middle] + word + string[middle:]
    return new_string

string = input("\n enter string : ")
>>>>>>> 889b1fe0cbadc5ed278321e19915062a98e3e16c
print("\n result : ",string_insert(string))