<<<<<<< HEAD
def postfix(string):
    if len(string) <= 3:
        return string
    elif string[-3:] == 'ing':
        string = string + "ly"
        return  string
    else:
        string = string + "ing"
        return string

print("Enter your value")
aa = input()
print("entered value : ",aa)
print("\n result : ",postfix(aa))
=======
def postfix(string):
    if len(string) <= 3:
        return string
    elif string[-3:] == 'ing':
        string = string + "ly"
        return  string
    else:
        string = string + "ing"
        return string

print("Enter your value")
aa = input()
print("entered value : ",aa)
print("\n result : ",postfix(aa))
>>>>>>> 889b1fe0cbadc5ed278321e19915062a98e3e16c
