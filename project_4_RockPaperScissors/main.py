import random


def rock_paper_scissors():
    print("r-rock; p-paper; s-scissors")
    user = input("Pick your choice ('r', 'p', 's'): ")
    computer = random.choice(['r','p','s'])
    #r<p, p<s, s>r
    if computer == user:
        print(f"We both chose {user}")
        return "It's a tie"

    if is_win(computer, user):
        print(f"I am poor {computer}!!\nYou won {user}")
        return 
    print(f"Haha! You lil {user}, I am the {computer}!! I WON!!!!")

def is_win(player, opponent):
    # return true if opponent wins
    if (player == 'r' and opponent == 'p') or (player == 'p' \
        and opponent == 's') or (player == 's' and opponent == 'r'):
        return True

rock_paper_scissors()