def word_counter(sentence):
    counts = dict()
    words_list = sentence.split(' ')
    for word in words_list:
        print("\n>> word : ",word)
        print("inside loop : ",counts)
        if word in counts:
            counts[word] += 1
            print("if : ",counts)
        else:
            counts[word] = 1
            print("else : ",counts)
    return counts


sentence = input("Enter your string: ")
print("\n result : ",word_counter(sentence))