def compare(list1,list2):
    common = set()
    count = 0
    result = False
    for word1 in list1:
        for word2 in list2:
            if word1 == word2:
                common.add(word1)
                result = True
                count += 1
    print("common : ",common)
    print("count : ",count)
    return result

list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9,2,3]
print("\nresult : ",compare(list1,list2))