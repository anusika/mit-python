# Problem Set 6: 
# Name: Anusika Nijher
# Collaborators: None
#Problem 1: 10 min 
#Problem 2: 10 min
#Problem 3: 1:30
#Problem 4: 2:30

import random
import string
import time
import itertools #use to get permutations of substrings for problem 4 yay!
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words1.txt"

def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

word_list = load_words()

def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def get_word_score(word):
    n = HAND_SIZE
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

def update_hand(hand, word):
    for x in word:
        hand[x] = hand[x] - 1
    return hand
    

def is_valid_word(word, hand):
    test_hand = hand.copy()
    for x in word:
        if (test_hand.get(x,0) == 0):
            return False
        else:
            test_hand[x] = test_hand[x]-1
    if (word in word_list):
        return True
    else:
        return False

def get_words_to_points():
    for word in word_list:
        points_dict[word] = get_word_score(word)
    print "points_dict has loaded"
    return points_dict

points_dict = {}
points_dict = get_words_to_points()


def get_time_limit(points_dict, k):
    start_time = time.time()
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word)
        end_time = time.time()
    return (end_time - start_time) * k

def pick_best_word(hand):
    best_word = ""
    best_word_score = 0
    for word in points_dict:
        if is_valid_word(word,hand):
            word_score = get_word_score(word)
            if word_score > best_word_score:
                best_word = word
                best_word_score = word_score
    if best_word_score > 0:
        print best_word
        return best_word
    else:
        print "no word could be made. Sorry!"
        return "."

def get_word_rearrangements():
    rearrange_dict = {}
    for word in word_list:
        rearrange_dict[''.join(sorted(word))] = word
    return rearrange_dict

rearrange_dict = {}
rearrange_dict = get_word_rearrangements()
   
def pick_best_word_faster(hand):    
    hand_string = ""
    best_word = ""
    best_score = 0
    attempts = 0
    for letter in hand.keys():
        if hand[letter] > 0:
            hand_string = hand_string + letter * hand[letter]
    hand_string=''.join(sorted(hand_string))
    substrings = list(itertools.chain.from_iterable([list(itertools.combinations(hand_string,i)) for i in range(2,len(hand_string))]))
    for possible in substrings:
        attempts = attempts + 1
        possible=''.join(sorted(possible))
        if is_valid_word(possible, hand):
            word_score = get_word_score(possible)
            if word_score > best_score:
                best_word = possible
                best_score = word_score
    if best_score > 0:
        best_word = rearrange_dict[best_word]
        print best_word
        print "attempts:",attempts
        return best_word
    else:
        print "attempts:",attempts
        print "no word could be made. Sorry!"
        return "."

def play_hand(hand, word_list):
    total_score = 0
    min_time = 0.010
    time_limit = get_time_limit(points_dict, 1)
    final_time = 0
    print" <-----------------------------NEW--HAND------------------------------>"
    print "You have", round(time_limit,2), "seconds"
    while True:
        print
        display_hand(hand)
        letters=0
        for key in hand.keys():
            for i in range(hand[key]):
                letters = letters + 1
        if letters == 1 or letters == 0:
            break
        start_time = time.time()
        word = pick_best_word_faster(hand)
        end_time=time.time()
        total_time = end_time - start_time
        if total_time < min_time:
            total_time = min_time
        print "It took", round(total_time,2), "seconds for your response"
        if (word =="."):
            break
        if (is_valid_word(word, hand)):
            hand_score = get_word_score(word)
            time_limit = time_limit - total_time
            if time_limit >= 0 :
                total_score = total_score + hand_score
                final_time = final_time + total_time
                update_hand(hand, word)
                print "Score for hand:", hand_score, "Total score so far:", total_score
                print "You have", round(time_limit,2), "seconds left!"
            else:
                print "opps you took too long"
                break
        else:
            time_limit = time_limit - total_time
            final_time = final_time + total_time
            if time_limit >= 0:
                print "Invalid Try Again! If you can't make a word press ."
                print "You have", round(time_limit,2), "seconds left!"
            else:
                print "oops you took too long and that was invalid lol"
                break
    print "Final Score is:", total_score
    print "Final Time was:", round(final_time,2)

def play_game():
    hand = deal_hand(HAND_SIZE)
    word_list = load_words()
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
    play_game()




