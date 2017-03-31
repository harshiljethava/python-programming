#!/usr/env/python
ran=int(input())
word_list=list()
string=str()
counter=list()

vowels=['A', 'E', 'I', 'O', 'U' ,'a','e','i','o' ,'u']
for i in range(ran):
    string=input()
    word_list.insert(i,string)

#print(word_list)

for i in range(ran):
    count=0
    for j in range(len(word_list[i])):
        for k in range(len(vowels)):
            if(word_list[i][j]==vowels[k]):
                count+=1
    counter.insert(i,count)
for i in range(len(counter)):
    print(counter[i])
