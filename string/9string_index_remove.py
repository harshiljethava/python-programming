def index_remove(word, n):
    first_part = word[:n]
    last_part = word[n + 1:]
    return first_part + last_part


string = str(input("Enter string value : "))
n = int(input("Enter index value to remove : "))

print("\n result : ", index_remove(string, n))
