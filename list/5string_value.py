def match_words(list):
    match = 0
    for words in list:
        if words[0] == words[-1] and len(words) > 2:
            match += 1
    return match


list = ['abcda', 'xyz', 'aba', '1221','qwerq' ]
print("List :", list)
print("\nresult : ", match_words(list))
