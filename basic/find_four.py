def list_count(num):
    count = 0
    for i in num:
        if i == 4:
            count = count + 1
    return count

print(list_count([1, 4, 6, 7, 4]))
print(list_count([1, 4, 6, 4, 7, 4]))