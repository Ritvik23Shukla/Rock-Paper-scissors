import random

def gameWinner(comp, player):
    if comp == player:
        return None

    elif comp == 'r':
        if player == 'p':
            return True
        elif player == 's':
            return False

    elif comp == 'p':
        if player == 'r':
            return False
        elif player == 's':
            return True

    elif comp == 's':
        if player == 'r':
            return True
        elif player == 'p':
            return False


print("Computer's turn: Rock(r), Paper(p), Scissors(s) ?")
randNo = random.randint(1,3)

if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

player = input("Your turn: Rock(r), Paper(p), Scissors(s) ?")
a = gameWinner(comp, player)

print(f"Computer chose {comp}")
print(f"You chose {player}")

if a == None:
    print("The game is tied")
elif a:
    print("You win")
else: 
    print("You loose")

