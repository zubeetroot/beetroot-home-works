#TASK1:
#Make a program that has some sentence (a string) on input and returns a dict
# containing all unique words as keys and the number of occurrences as values.

sentence = input("Enter a sentence: ")
print(sentence)

def count_words(sentence):           # just a simple word counter
    words = sentence.split()
    if len(words) < 2:
        print("Please enter at least two words")
    else:
        return len(words)
print("How many words: ", count_words(sentence))

def count_words(sentence):          # proper dictionary
    sentence.lower()
    words = sentence.split()
    word_occurrences = {}
    for word in words:
        if word in word_occurrences:
            word_occurrences[word] += 1
        else:
            word_occurrences[word] = 1

    return word_occurrences
word_counts = count_words(sentence)
print(word_counts)



#TASK 2
#Create a function which takes as input two dicts with structure mentioned above,
# then computes and returns the total price of stock.


import random
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
def compute_total_price(stock, prices):
    total_price = 0
    for key in stock.keys():
        total_price += stock[key] * prices[key]
        print(f"{key}: {stock[key]} * {prices[key]}")
    return total_price
print(compute_total_price(stock, prices))

#TASK 3
#List comprehension exercise
# Use a list comprehension to make a list containing tuples (i, j)
# where i goes from 1 to 10 and j is corresponding to i squared.

tuple_list = []
for i in range(1, 10):
   for j in range(i ** 2):
       tuple_list.append((i, j))

print(tuple_list)
