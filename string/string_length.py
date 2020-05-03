def str_length(string):
    count = 0
    for i in string:
        count += 1
    return count

str_value = input("Enter your string")
print("string length : ",str_length(str_value))