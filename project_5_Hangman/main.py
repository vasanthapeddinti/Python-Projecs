from words import words
import random
import string

def get_valid_word(words):
    computer_word = random.choice(words)
    while '-' in computer_word or ' ' in computer_word:
        computer_word = random.choice(words)
    print(computer_word)#debug
    return computer_word.upper()

def hangman(words):
    word = get_valid_word(words)
    word_letters = set(word) 
    used_letters = set()
    alphabets = set(string.ascii_uppercase)

    lives = 6

    while len(word_letters)> 0 and lives>0:
        #letters used
        # ' '.join(['a', 'b']) = 'a b'
        print("\nYou have used these letters: ", ' '.join(used_letters))

        word_letter= []
        #What current word is? (W _ R D) [can be done in list comprehension as well]
        for letter in word:
            if letter in used_letters:
                word_letter.append(letter)
            else:
                word_letter.append("_")
        print("Current Word", ' '.join(word_letter))

        #User's input
        print(f"You have {lives} lives left!")
        user_input = input("\nGuess a letter: ").upper()
        if user_input in alphabets - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives = lives - 1# take away life when guessed wrong, or repeated letter or invalid character
            
        elif user_input in used_letters:
            print("You have already used the letter!!")
            lives = lives - 1
        else:
            print("Invalid character!")
            lives = lives - 1
    if lives == 0:
        print("Sorry! You died!! Play again!!!")
    else:
        print("Congrats you have guessed the word!")
hangman(words)
