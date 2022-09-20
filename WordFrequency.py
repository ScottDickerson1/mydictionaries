import string

#WordFrequency.py - Write a program that reads the contents of a text file (you can use this file - sometext.txt  Download sometext.txt). 
#The program should create a dictionary in which the keys are the individual words found in the file and the values are the 
#number of times each word appears. 
#For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
#The program should display the frequency of each word.

infile = open('sometext.txt', 'r')

text = {}

for rec in infile:
    rec = rec.strip()
    rec = rec.lower()
    words = rec.split(' ')
    for word in words:
        if word in text:
            text[word] = text[word] + 1
        else: 
            text[word] = 1

print('word: frequency')
for key in text:
    print(key.translate(str.maketrans('', '', string.punctuation)) + ': ' + str(text[key]))
