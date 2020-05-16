
def duplicate(list):
    dup_items = set()
    unique_items = []
    for item in list:
        if item not in dup_items:
            unique_items.append(item)
            dup_items.add(item)
    return unique_items

list = [10,20,30,20,10,50,60,40,80,50,40]
print("list : ",list)
print("\nresult : ",duplicate(list))