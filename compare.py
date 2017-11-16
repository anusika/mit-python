WORDLIST_FILENAME = "words.txt"
WORDLIST_FILENAME2 = "oxford.txt"
def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip())
    print "  ", len(wordlist), "words loaded."
    return wordlist
#longer
def load_words2():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME2, 'r', 0)
    wordlist2 = []
    for line in inFile:
        wordlist2.append(line.strip())
    print "  ", len(wordlist2), "words loaded."
    return wordlist2


wordlist = load_words()
wordlist_oxford=load_words2()


def compare(wordlist_oxford,wordlist):
    notin = open("notin.txt", "w")
    word_notin = []
    for word in wordlist_oxford:
        if word not in wordlist:
            word_notin.append(word)
            notin.write(word + '\n')
    notin.close()
    return word_notin


compare(wordlist_oxford,wordlist)
