print("exception handling")
print("python has more than 70 in built excpetion handling class")
try:
    print("You are in Try block ")
except Exception as e:
    print("except ",e)
    
else:
    print("else block ")
finally:
    print("finally block ")

i=0;j=12
try:
    print("i:",i,"||"," j:",j)
    k=j/i
except ZeroDivisionError as ze:
    print(ze)
finally:
    print("finally block")

print("python provide 3 way to make custom excpetion")
print("1. raise exception(arg)\n2. raise exception(arg) from original\
\n3. raise")
