My Solutions to MIT 6.00 Python 2.7 Assigments
A Note on the word documents:

MIT provided a word document (currently called words1.txt) that contains 83668 words.This was good for smaller, simpler games.
However after a simple Google there appears to be 171,476 words in the English dictionary.
This lead to the use of words.txt which (original link found: http://www.gwicks.net/dictionaries.htm) contains
194,433 words. This added a bit of a new challenge with guessing what possible words could come next in the ghost game.
But we can go deeper. 
https://github.com/dwyl/english-words.

This github repo has a txt file with 370,099 English words. This is stored in oxford.txt
I used this massive word list for the ghost game (ps5_ghost.py) to add this awesome level of
complexity where not even the players know all the possible words. It's also 
really fun to lose to a random word that you do not even know the meaning of.
