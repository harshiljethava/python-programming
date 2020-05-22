def reverse_string(string):
    if (len(string) % 4) == 0:
        new_string = ''.join(reversed(string))
        return new_string

print("enter string : ")
string = input()
print("\n result : ",reverse_string(string))
