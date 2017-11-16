# Problem Set 5: Ghost
# Name: Anusika Nijher
# Collaborators: None
# Time: 2 hours

import random
import string

WORDLIST_FILENAME = "oxford.txt"

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

rules = """Rules of Ghost 
Players form a word by alternating turns saying a letter, which is added on to the end of the word \n
fragment. There are two ways to lose Ghost:\n
***Forming a word longer than 3 letters ("PEA" is ok, but "PEAR" is not).\n
***Creating a fragment (of any size) which cannot become a word by adding more letters (for
example, "QZ"). \n
Winning Ghost is simply not losing! So, for example, game play proceeds like this:\n
Player 1 says a letter. For example, 'P'.\n
Player 2 says a letter. For example, 'E'.\n
Player 1 says a letter. For example, 'A'. Player 1 has formed the word PEA, but that's okay
because it is not longer than 3 letters.\n
Player 2 says a letter. For example, 'F'.\n
Player 1 says a letter. Player 1 must say 'O', because only one word starts with PEAF. If Player 1
says any other letter, for example 'A', he or she loses, because no word begins with PEAFA.\n
Player 2 says a letter, which must be 'W'.\n
Player 1 says a letter, which must be 'L'. Player 1 loses, because PEAFOWL is a word.\n
"""

def turn(current_player):
    if (current_player == 1):
        return 2
    else: return 1


def is_valid(current_word, word_list):
    top = len(current_word)
    for word in word_list:
        if (word[0:top] == current_word):
            if (len(word) > len(current_word)):
                return "usable fragment"
            elif(len(word) == len(current_word) and len(current_word) > 3):
                return "too long"




def ghost():
    wins1 = 0
    wins2 = 0
    current_player = 2
    x = 1
    wordlist = load_words()

    print rules
    while(x == 1):
        word_fragment=[]
        current_word = ""
        while (x == 1):
            print 
            print "current_player is", turn(current_player)
            current_player = turn(current_player)
            print "current word is", current_word
            word_fragment.append(raw_input("Give me a letter").lower())
            print 
            print "checking..."
            current_word = "".join(word_fragment)
            if(word_fragment[-1].isalpha() == False):
                print "Opps! Give me a letter"
                del word_fragment[-1]
                current_word = current_word[:-1]
                
            elif(len(word_fragment) == 1 and current_word in string.ascii_letters):
               current_word.join(word_fragment)
               print "so good so far!"
               continue

            elif(is_valid(current_word, wordlist) == "too long"):
                print current_word
                print "Oh no! Player", current_player, "made a word longer than 3 letters! They lose!"
                print "Player", turn(current_player),"wins!"
                if(current_player == 1):
                    wins2 = wins2 + 1
                else:
                    wins1 = wins1 + 1 
                print "current score: Player 1:", wins1, "Player 2:", wins2
                break

                    
            elif(is_valid(current_word, wordlist) == "usable fragment"):
                print "Okay we can work with this"
                continue
            
            elif(is_valid(current_word, wordlist) != "usable fragment"):
                print "We can't use this fragment!"
                print "Player", current_player, "loses!"
                print "Player", turn(current_player), "wins!"
                if(current_player ==  1):
                    wins2 = wins2 + 1
                else:
                    wins1 = wins1 + 1
                print "current score: Player 1:", wins1, "Player 2:", wins2
                break


            else:
                print "How did you get here?"
                break

        x = int(input("\nNew Game? Press 1: Exit? Press 0"))
        if(x == 0):
            print "final score: Player 1:", wins1, "Player 2:", wins2
 

    


                            
if __name__ == '__main__':
    ghost()


