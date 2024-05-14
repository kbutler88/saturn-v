import random

def roll_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!\n")
    return roll

while True:
    players = input("How many players? (2-4): ")
    if players == "2" or players == "3" or players == "4":
        players = int(players)
        print()
        break
    else:
        print("Please enter a valid number of players.")

total_score = []

# Set each player's score to 0
for i in range(players):
    total_score.append(0)

while max(total_score) < 50:
    for i in range(players):
        this_score = total_score[i]
        print("Player " + str(i + 1) + "'s turn.")
        input("Press Enter to roll the dice.")
        while True:
            print()
            this_roll = roll_dice()
            if this_roll == 1:
                print("Sorry, but your turn is over.")
                print("Your score is " + str(total_score[i]) + "\n")
                break
            this_score += this_roll
            if input("Would you like to roll again? (y) ").lower() == 'n':
                total_score[i] = this_score
                print(f"Your score is: {total_score[i]}\n")
                break

print("Player " + str(total_score.index(max(total_score)) + 1) + " wins!!\n")