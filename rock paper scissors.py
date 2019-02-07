import random
import time

rock = 1
paper = 2
scissors = 3

name = { rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = { 1 : 3, 2 : 1, 3 : 2}

player_score = 0
computer_score = 0

def start():
    print("Let's play a game of rock, Paper, Scissors")
    while game():
        pass
    scores()

def  game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print()
        player = input("Rock = 1 \nPaper = 2 \nScissors = 3\nMake your move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("Oops! I didn't understand that. Please enter 1,2,3.")

def result(player, computer):
    print("1 . . .")
    time.sleep(1)
    print("2 . . .")
    time.sleep(1)
    print("3 . . .")
    time.sleep(0.5)
    print("Computer threw {}!" .format(name[computer]))
    global player_score, computer_score
    if player == computer:
        print("Tie game.")
    else:
        if rules[player] == computer:
            print("Your victory has been assured")
            player_score += 1
        else:
            print("Hahaha, you lost, Accept Defeat!")
            computer_score += 1

def play_again():
    answer = input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "Of Course!"):
        return answer
    else:
          print("\nThank You very much for playing our game. See you next time!")

def scores():
    global player_score, computer_score
    print("HIGH SCORES")
    print("Player: ", player_score)
    print("Computer: ", computer_score)

if __name__ == "__main__":
    start()
