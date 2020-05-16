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
print("\nresult : ",find_word(string))