<<<<<<< HEAD
def find_word(string):
    new_list = string.split(' ')
    n = int(input("enter length of word for search :"))
    found_word = set()
    for word in new_list:
        if len(word) > n:
            found_word.add(word)
        else:
            pass
    return found_word

string = input("Enter your sentence : ")
=======
def find_word(string):
    new_list = string.split(' ')
    n = int(input("enter length of word for search :"))
    found_word = set()
    for word in new_list:
        if len(word) > n:
            found_word.add(word)
        else:
            pass
    return found_word

string = input("Enter your sentence : ")
>>>>>>> 889b1fe0cbadc5ed278321e19915062a98e3e16c
print("\nresult : ",find_word(string))