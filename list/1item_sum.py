def item_sum(lists):
    sum = 0
    for i in lists:
        sum += i
    return  sum
lists = [1,2,3,4,5,6,7]
print("list : ",lists)
print("sum : ",item_sum(lists))
