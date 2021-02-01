# Mad Libs is a phrasal template word game which consists of one player 
# prompting others for a list of words to substitute for blanks in a story 
# before reading aloud. The game is frequently played as a party game or as 
# a pastime.

noun_1 = input("noun: ")
Animal = input("animal: ")
verb_1 = input("verb: ")
Place = input("Place: ")
adjective = input("adjective: ")
verb_2 = input("verb: ")
Game = input("Game: ")
verb_3 = input("verb: ")
noun_2 = input("noun: ")

madlib = f"All of my {noun_1}, I wanted a {Animal} to {verb_1} within the {Place} \
A {Animal} would be so {adjective}, soft and cuddly. We would {verb_2}, {Game} \
together every afternoon and she would {verb_3} next to my {noun_2} at night."


print(madlib)