def is_group_member(group,n):
    for value in group:
        if n == value:
            return True
    return False

print(is_group_member([1, 5, 8, 3], 3))
print(is_group_member([5, 8, 3], -1))
print(is_group_member([6, 7, 3, 1], 3))
print(is_group_member([5, 8, 1], -1))