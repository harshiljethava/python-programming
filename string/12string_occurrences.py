<<<<<<< HEAD
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
=======
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
>>>>>>> 889b1fe0cbadc5ed278321e19915062a98e3e16c
print("\n result : ",word_counter(sentence))