# Problem Set 5: 
# Name: Anusika Nijher
# Collaborators: None

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

#
# Problem #1: Scoring a word
#Time: 10 min
def get_word_score(word, n):
    total = 0
    for x in word:
        total = total + SCRABBLE_LETTER_VALUES[x]
    if (len(word) == n):
        total = total + 50
    return total


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              
    print                              

def deal_hand(n):
    hand={}
    num_vowels = n / 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand


# Problem #2: Update a hand by removing letters
#Time: 10 min
def update_hand(hand, word):
    for x in word:
        hand[x] = hand[x] - 1
    return hand
    

# Problem #3: Test word validity
# Time: 15 min
def is_valid_word(word, hand, word_list):
    test_hand = hand.copy()
    for x in word:
        if (test_hand.get(x,0) == 0):
            return False
        else:
            test_hand[x] = test_hand[x]-1
            
    if(word.lower() in word_list):
         return True
    else:
        return False

#
# Problem #4: Playing a hand
# Time: 20min
def play_hand(hand, word_list):
    total_score = 0
    while True:
        print 
        display_hand(hand)
        letters=0
        for key in hand.keys():
            for i in range(hand[key]):
                letters = letters + 1
        if letters == 1 or letters == 0:
            break
        word = raw_input("Give a word!")
        word = word.lower()
        if (len(hand) <= 1):
            break
        if (word =="."):
            break
        if (is_valid_word(word, hand, word_list)):
            hand_score = get_word_score(word, HAND_SIZE)
            total_score = total_score + hand_score
            update_hand(hand, word) 
            print "Score for hand:", hand_score, "Total score so far:", total_score
        else:
            print "Invalid Try Again! If you can't make a word press ."
    print "Final Score is:", total_score
    
#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list):
    hand = deal_hand(HAND_SIZE) 
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        cmd = cmd.lower()
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
