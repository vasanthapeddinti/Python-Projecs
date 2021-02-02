import random

def guess(x):
    random_number = random.randint(1, x)
    print(f"\nAbracadabra.. Abracadabra..\nI have chosen a number between 1 and {x}")
    print("Can you guess it!!!")
    
    guess = 0
    while(guess != random_number):
        guess = int(input("\n\nWhat do you think the number is..ha! "))
        if guess > random_number:
            print("\n\nYou need to calm down.. :P\nGuess a lil lower")
        else:
            print("\n\nWhat the hell!!\nHow can you guess this low?")
    else:
        print(f"\n\n\nPerfect Bro! {random_number} is the right answer!!!")

number = int(input("\nSelect a positive integer (no zero please!): "))
guess(number)
