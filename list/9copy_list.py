def copy_list(old_list):
    new_list = list(old_list)
    return new_list

old_list = [10, 22, 44, 23, 4]
print("old list :",old_list)
print("\nresult : ",copy_list(old_list))