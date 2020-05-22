def odd_index_remove(string):
    result = ""
    for i in range(len(string)):
        if i % 2 == 0:
            result = result + string[i]
    return result

string = str(input("Enter your string : "))
print("\n result : ",odd_index_remove(string))