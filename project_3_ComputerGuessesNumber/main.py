import random

def computer_guess(x):
    print("\nThink of a positive integer in your mind!! I will guess it for you...:)")
    
    feedback = ''
    low = 1
    high = x

    while feedback != 'right':
        guess = random.randint(low, high)
        feedback = input(f"\nIs {guess} 'low' or 'high' or 'right'? ")
        if feedback == 'low':
            low = guess + 1
        elif feedback == 'high':
            high = guess - 1
    print("\n\nThank God! I guessed it right!\n") 

max_number = int(input("Provide a max_number: "))
computer_guess(max_number)