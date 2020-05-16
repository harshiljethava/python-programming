def max_value(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max
list = [1,2,3,7,4,99,24]
print("list : ",list)
print("result : ",max_value(list))