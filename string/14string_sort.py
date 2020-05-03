def string_sort(string):
    new_string = string.split(",")
    print("\n Result : ")
    print(",".join(sorted(list(set(new_string)))))


string = input("enter value with comma separated : ")
result = string_sort(string)

