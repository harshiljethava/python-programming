x=0
if x>-1:
    print("big")
else:
    print("small")

count=int(input("enter file no"))
print("{0} file{1}".format((count if count !=0 else "no"),("s" if count !=1 else "")))
print("enter name")
name=input()
print(name if name=="harshil" else "jarvis")
