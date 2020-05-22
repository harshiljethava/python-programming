<<<<<<< HEAD
def odd_index_remove(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return result

string = str(input("Enter your string : "))
=======
def odd_index_remove(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return result

string = str(input("Enter your string : "))
>>>>>>> 889b1fe0cbadc5ed278321e19915062a98e3e16c
print("\n result : ",odd_index_remove(string))