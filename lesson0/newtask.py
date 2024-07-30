


#Make a program that has some sentence (a string) on input and returns a dict containing all unique words as keys and the number of occurrences as values.


def word_count(str):
    counts = dict()

    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print( word_count('To już ten moment. Czas na otwarcie igrzysk olimpijskich'))

