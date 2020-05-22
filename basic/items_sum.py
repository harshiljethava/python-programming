def item_sum(items):
    sum_numbers = 0
    for i in items:
        sum_numbers += i
    return sum_numbers

print("sum : ",item_sum([1,2,3,4,-6]))
print("sum : ",item_sum([11,2,3,4,-6]))

def zero_sum(x,y,z):
    if x == y or y == z or z == x :
        sum = 0
    else:
        sum = x + y + z
    return sum

print(zero_sum(1,2,3))
print(zero_sum(3,2,3))
print(zero_sum(1,1,3))

