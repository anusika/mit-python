
def compare():
    notin = open("notin.txt", "w")
    word_notin = ['a','b','c']
    for word in word_notin:
        notin.write(word + '\n')
    notin.close()
    return word_notin

compare()
