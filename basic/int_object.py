def int_add(x,y):
    if type(x) == int and type(y) == int:
        sum = x + y
        return sum
    else:
        return "object type is not int"

print("\nresult : ",int_add(10,20))
print("\nresult : ",int_add('0',20))