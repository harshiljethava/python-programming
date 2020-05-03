def find_word_length(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
        print("Appending : ", word_len)
    word_len.sort()
    print("\nSorted : ", word_len)
    return word_len[-1][1]


print(find_word_length(["PHP", "Exercises", "Backend"]))
