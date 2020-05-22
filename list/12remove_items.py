def item_remove(list1):
    remove_count = int(input("How many item you want to remove?"))
    index_set = []
    for i in range(remove_count):
        temp = int(input("enter index value : "))
        index_set.append(temp)
    print("removing value from list1...")
    for i in range(len(list1)):
        del list1[index_set[i]]
    return list1

list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("list : ",list1)
print("result : ",item_remove(list1))